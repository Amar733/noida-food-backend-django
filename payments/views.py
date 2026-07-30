from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from .models import Payment
from orders.models import Order
from .schemas import PaymentSchema, CreatePaymentSchema, PaymentStatusUpdateSchema
from users.views import AuthBearer

router = Router()


@router.get("/payments", response=List[PaymentSchema], auth=AuthBearer())
def list_payments(request):
    """Get user's payment history"""
    payments = Payment.objects.filter(user=request.auth).select_related('order')
    
    return [{
        "id": payment.id,
        "order_id": payment.order.id,
        "order_number": payment.order.order_number,
        "amount": payment.amount,
        "payment_method": payment.payment_method,
        "status": payment.status,
        "transaction_id": payment.transaction_id,
        "payment_gateway": payment.payment_gateway,
        "created_at": payment.created_at,
        "updated_at": payment.updated_at
    } for payment in payments]


@router.get("/payments/{payment_id}", response=PaymentSchema, auth=AuthBearer())
def get_payment(request, payment_id: int):
    """Get payment details"""
    payment = get_object_or_404(
        Payment.objects.select_related('order'),
        id=payment_id,
        user=request.auth
    )
    
    return {
        "id": payment.id,
        "order_id": payment.order.id,
        "order_number": payment.order.order_number,
        "amount": payment.amount,
        "payment_method": payment.payment_method,
        "status": payment.status,
        "transaction_id": payment.transaction_id,
        "payment_gateway": payment.payment_gateway,
        "created_at": payment.created_at,
        "updated_at": payment.updated_at
    }


@router.post("/payments", response={201: PaymentSchema}, auth=AuthBearer())
def create_payment(request, payload: CreatePaymentSchema):
    """Create payment for order"""
    user = request.auth
    order = get_object_or_404(Order, id=payload.order_id, user=user)
    
    # Check if payment already exists
    if hasattr(order, 'payment'):
        return 400, {"error": "Payment already exists for this order"}
    
    payment = Payment.objects.create(
        order=order,
        user=user,
        amount=order.total_amount,
        payment_method=payload.payment_method,
        transaction_id=payload.transaction_id,
        payment_gateway=payload.payment_gateway,
        status='pending'
    )
    
    return 201, get_payment(request, payment.id)


@router.patch("/payments/{payment_id}", response=PaymentSchema, auth=AuthBearer())
def update_payment_status(request, payment_id: int, payload: PaymentStatusUpdateSchema):
    """Update payment status"""
    payment = get_object_or_404(Payment, id=payment_id)
    
    payment.status = payload.status
    if payload.transaction_id:
        payment.transaction_id = payload.transaction_id
    
    payment.save()
    
    # Update order status based on payment
    if payment.status == 'completed':
        payment.order.status = 'processing'
        payment.order.save()
    elif payment.status == 'failed':
        payment.order.status = 'cancelled'
        payment.order.save()
    
    return get_payment(request, payment_id)


@router.post("/payments/{payment_id}/verify", auth=AuthBearer())
def verify_payment(request, payment_id: int, transaction_data: dict):
    """Verify payment from payment gateway"""
    payment = get_object_or_404(Payment, id=payment_id, user=request.auth)
    
    # Here you would integrate with actual payment gateway
    # For now, we'll simulate verification
    
    payment.gateway_response = transaction_data
    payment.status = 'completed'
    payment.save()
    
    # Update order status
    payment.order.status = 'processing'
    payment.order.save()
    
    return {"message": "Payment verified successfully", "payment": get_payment(request, payment_id)}

