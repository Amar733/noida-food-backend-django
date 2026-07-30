from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import Cart, CartItem, Order, OrderItem
from products.models import Product
from .schemas import (
    CartSchema, CartItemSchema, AddToCartSchema, UpdateCartItemSchema,
    OrderSchema, OrderListSchema, CreateOrderSchema, UpdateOrderStatusSchema
)
from users.views import AuthBearer
import uuid

router = Router()


# Cart endpoints
@router.get("/cart", response=CartSchema, auth=AuthBearer())
def get_cart(request):
    """Get user's cart"""
    user = request.auth
    cart, created = Cart.objects.get_or_create(user=user)
    
    items_data = []
    for item in cart.items.select_related('product'):
        items_data.append({
            "id": item.id,
            "product_id": item.product.id,
            "product_name": item.product.name,
            "product_image": item.product.image.url if item.product.image else None,
            "price": item.product.price,
            "quantity": item.quantity,
            "subtotal": item.subtotal
        })
    
    return {
        "id": cart.id,
        "items": items_data,
        "total": cart.total,
        "items_count": cart.items_count
    }


@router.post("/cart", response={201: CartSchema}, auth=AuthBearer())
def add_to_cart(request, payload: AddToCartSchema):
    """Add product to cart"""
    user = request.auth
    cart, created = Cart.objects.get_or_create(user=user)
    product = get_object_or_404(Product, id=payload.product_id)
    
    if product.stock < payload.quantity:
        return 400, {"error": "Insufficient stock"}
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': payload.quantity}
    )
    
    if not created:
        cart_item.quantity += payload.quantity
        if product.stock < cart_item.quantity:
            return 400, {"error": "Insufficient stock"}
        cart_item.save()
    
    return 201, get_cart(request)


@router.put("/cart/{item_id}", response=CartSchema, auth=AuthBearer())
def update_cart_item(request, item_id: int, payload: UpdateCartItemSchema):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.auth)
    
    if cart_item.product.stock < payload.quantity:
        return 400, {"error": "Insufficient stock"}
    
    cart_item.quantity = payload.quantity
    cart_item.save()
    
    return get_cart(request)


@router.delete("/cart/{item_id}", auth=AuthBearer())
def remove_from_cart(request, item_id: int):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.auth)
    cart_item.delete()
    return {"message": "Item removed from cart"}


@router.delete("/cart", auth=AuthBearer())
def clear_cart(request):
    """Clear entire cart"""
    cart = get_object_or_404(Cart, user=request.auth)
    cart.items.all().delete()
    return {"message": "Cart cleared"}


# Order endpoints
@router.get("/orders", response=List[OrderListSchema], auth=AuthBearer())
def list_orders(request):
    """Get user's orders"""
    orders = Order.objects.filter(user=request.auth).order_by('-created_at')
    return orders


@router.get("/orders/{order_id}", response=OrderSchema, auth=AuthBearer())
def get_order(request, order_id: int):
    """Get order details"""
    order = get_object_or_404(
        Order.objects.prefetch_related('items__product'),
        id=order_id,
        user=request.auth
    )
    
    items_data = []
    for item in order.items.all():
        items_data.append({
            "id": item.id,
            "product_id": item.product.id,
            "product_name": item.product.name,
            "quantity": item.quantity,
            "price": item.price,
            "subtotal": item.subtotal
        })
    
    return {
        "id": order.id,
        "order_number": order.order_number,
        "total_amount": order.total_amount,
        "status": order.status,
        "shipping_address": order.shipping_address,
        "shipping_city": order.shipping_city,
        "shipping_state": order.shipping_state,
        "shipping_zip": order.shipping_zip,
        "shipping_phone": order.shipping_phone,
        "tracking_number": order.tracking_number,
        "items": items_data,
        "created_at": order.created_at,
        "updated_at": order.updated_at
    }


@router.post("/orders", response={201: OrderSchema}, auth=AuthBearer())
@transaction.atomic
def create_order(request, payload: CreateOrderSchema):
    """Create order from cart"""
    user = request.auth
    cart = get_object_or_404(Cart, user=user)
    
    if not cart.items.exists():
        return 400, {"error": "Cart is empty"}
    
    # Check stock availability
    for item in cart.items.select_related('product'):
        if item.product.stock < item.quantity:
            return 400, {"error": f"Insufficient stock for {item.product.name}"}
    
    # Create order
    order = Order.objects.create(
        user=user,
        order_number=f"ORD-{uuid.uuid4().hex[:8].upper()}",
        total_amount=cart.total,
        shipping_address=payload.shipping_address,
        shipping_city=payload.shipping_city,
        shipping_state=payload.shipping_state,
        shipping_zip=payload.shipping_zip,
        shipping_phone=payload.shipping_phone,
        notes=payload.notes
    )
    
    # Create order items and update stock
    for item in cart.items.select_related('product'):
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
        
        # Update stock
        item.product.stock -= item.quantity
        item.product.save()
    
    # Clear cart
    cart.items.all().delete()
    
    return 201, get_order(request, order.id)


@router.patch("/orders/{order_id}", response=OrderSchema, auth=AuthBearer())
def update_order_status(request, order_id: int, payload: UpdateOrderStatusSchema):
    """Update order status (admin only)"""
    order = get_object_or_404(Order, id=order_id)
    order.status = payload.status
    
    if payload.tracking_number:
        order.tracking_number = payload.tracking_number
    
    order.save()
    return get_order(request, order_id)


@router.delete("/orders/{order_id}", auth=AuthBearer())
def cancel_order(request, order_id: int):
    """Cancel order"""
    order = get_object_or_404(Order, id=order_id, user=request.auth)
    
    if order.status not in ['pending', 'processing']:
        return 400, {"error": "Order cannot be cancelled"}
    
    order.status = 'cancelled'
    order.save()
    
    # Restore stock
    for item in order.items.select_related('product'):
        item.product.stock += item.quantity
        item.product.save()
    
    return {"message": "Order cancelled successfully"}

