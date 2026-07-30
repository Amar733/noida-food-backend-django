from ninja import Schema
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


class CartItemSchema(Schema):
    id: int
    product_id: int
    product_name: str
    product_image: Optional[str]
    price: Decimal
    quantity: int
    subtotal: Decimal

    class Config:
        from_attributes = True


class CartSchema(Schema):
    id: int
    items: List[CartItemSchema]
    total: Decimal
    items_count: int

    class Config:
        from_attributes = True


class AddToCartSchema(Schema):
    product_id: int
    quantity: int = 1


class UpdateCartItemSchema(Schema):
    quantity: int


class OrderItemSchema(Schema):
    id: int
    product_id: int
    product_name: str
    quantity: int
    price: Decimal
    subtotal: Decimal

    class Config:
        from_attributes = True


class OrderSchema(Schema):
    id: int
    order_number: str
    total_amount: Decimal
    status: str
    shipping_address: str
    shipping_city: str
    shipping_state: str
    shipping_zip: str
    shipping_phone: str
    tracking_number: Optional[str] = None
    items: List[OrderItemSchema]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OrderListSchema(Schema):
    id: int
    order_number: str
    total_amount: Decimal
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class CreateOrderSchema(Schema):
    shipping_address: str
    shipping_city: str
    shipping_state: str
    shipping_zip: str
    shipping_phone: str
    notes: Optional[str] = ""


class UpdateOrderStatusSchema(Schema):
    status: str
    tracking_number: Optional[str] = None
