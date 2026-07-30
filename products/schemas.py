from ninja import Schema
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


class CategorySchema(Schema):
    id: int
    name: str
    slug: str
    description: str
    image: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True


class CategoryCreateSchema(Schema):
    name: str
    slug: str
    description: Optional[str] = ""
    is_active: Optional[bool] = True


class ProductImageSchema(Schema):
    id: int
    image: str
    alt_text: str
    is_primary: bool

    class Config:
        from_attributes = True


class ProductListSchema(Schema):
    id: int
    name: str
    slug: str
    price: Decimal
    compare_price: Optional[Decimal] = None
    stock: int
    image: Optional[str] = None
    is_featured: bool
    discount_percentage: int
    category: CategorySchema

    class Config:
        from_attributes = True


class ProductDetailSchema(Schema):
    id: int
    name: str
    slug: str
    description: str
    price: Decimal
    compare_price: Optional[Decimal] = None
    stock: int
    image: Optional[str] = None
    is_active: bool
    is_featured: bool
    discount_percentage: int
    category: CategorySchema
    images: List[ProductImageSchema]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductCreateSchema(Schema):
    category_id: int
    name: str
    slug: str
    description: str
    price: Decimal
    compare_price: Optional[Decimal] = None
    stock: int
    is_active: Optional[bool] = True
    is_featured: Optional[bool] = False


class ReviewSchema(Schema):
    id: int
    user_id: int
    username: str
    rating: int
    comment: str
    created_at: datetime

    class Config:
        from_attributes = True


class ReviewCreateSchema(Schema):
    product_id: int
    rating: int
    comment: str


class WishlistSchema(Schema):
    id: int
    product: ProductListSchema
    created_at: datetime

    class Config:
        from_attributes = True


class WishlistAddSchema(Schema):
    product_id: int
