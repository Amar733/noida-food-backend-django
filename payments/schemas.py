from ninja import Schema
from typing import Optional
from datetime import datetime
from decimal import Decimal


class PaymentSchema(Schema):
    id: int
    order_id: int
    order_number: str
    amount: Decimal
    payment_method: str
    status: str
    transaction_id: Optional[str] = None
    payment_gateway: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CreatePaymentSchema(Schema):
    order_id: int
    payment_method: str
    transaction_id: Optional[str] = None
    payment_gateway: Optional[str] = None


class PaymentStatusUpdateSchema(Schema):
    status: str
    transaction_id: Optional[str] = None
