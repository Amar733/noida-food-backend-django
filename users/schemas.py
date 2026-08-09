from ninja import Schema
from typing import Optional
from datetime import datetime


class UserRegisterSchema(Schema):
    full_name: str
    phone: str
    password: str


class UserLoginSchema(Schema):
    phone: str
    password: str


class UserOutSchema(Schema):
    id: int
    phone: str
    first_name: str
    last_name: str
    address: str
    date_joined: datetime

    class Config:
        from_attributes = True


class TokenSchema(Schema):
    access: str
    refresh: str


class MessageSchema(Schema):
    message: str


class ErrorSchema(Schema):
    error: str
