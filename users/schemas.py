from ninja import Schema
from typing import Optional
from datetime import datetime


class UserRegisterSchema(Schema):
    username: str
    email: str
    password: str
    phone: Optional[str] = None
    address: Optional[str] = None


class UserLoginSchema(Schema):
    username: str
    password: str


class UserOutSchema(Schema):
    id: int
    username: str
    email: str
    phone: str
    address: str
    first_name: str
    last_name: str
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
