from ninja import Router
from ninja.pagination import paginate
from typing import List
from django.shortcuts import get_object_or_404
from .models import Category, Product, Review, Wishlist, ProductImage
from .schemas import (
    CategorySchema, CategoryCreateSchema,
    ProductListSchema, ProductDetailSchema, ProductCreateSchema,
    ReviewSchema, ReviewCreateSchema,
    WishlistSchema, WishlistAddSchema
)
from users.views import AuthBearer

router = Router()


# Category endpoints
@router.get("/categories", response=List[CategorySchema])
def list_categories(request):
    """Get all active categories"""
    return Category.objects.filter(is_active=True)


@router.get("/categories/{slug}", response=CategorySchema)
def get_category(request, slug: str):
    """Get category by slug"""
    return get_object_or_404(Category, slug=slug, is_active=True)


@router.post("/categories", response={201: CategorySchema}, auth=AuthBearer())
def create_category(request, payload: CategoryCreateSchema):
    """Create a new category (admin only)"""
    category = Category.objects.create(**payload.dict())
    return 201, category


# Product endpoints
@router.get("/products", response=List[ProductListSchema])
@paginate
def list_products(request, category: str = None, is_featured: bool = None, search: str = None, exclude_category: str = None):
    """Get all products with optional filters"""
    products = Product.objects.filter(is_active=True).select_related('category')
    
    if category:
        products = products.filter(category__slug=category)
    
    if exclude_category:
        products = products.exclude(category__slug=exclude_category)
    
    if is_featured is not None:
        products = products.filter(is_featured=is_featured)
    
    if search:
        products = products.filter(name__icontains=search)
    
    return products


@router.get("/products/featured/mixed", response=List[ProductListSchema])
def get_mixed_featured_products(request, limit: int = 8):
    """Get a balanced mix of featured products from different categories including sweets"""
    from django.db.models import Count
    import random
    
    # Get featured products grouped by category
    categories = Category.objects.filter(
        is_active=True,
        products__is_featured=True,
        products__is_active=True
    ).distinct()
    
    featured_products = []
    products_per_category = max(1, limit // categories.count()) if categories.count() > 0 else 1
    
    for category in categories:
        category_products = list(
            Product.objects.filter(
                category=category,
                is_featured=True,
                is_active=True
            )[:products_per_category]
        )
        featured_products.extend(category_products)
    
    # Shuffle to mix categories
    random.shuffle(featured_products)
    
    return featured_products[:limit]


@router.get("/products/{slug}", response=ProductDetailSchema)
def get_product(request, slug: str):
    """Get product details by slug"""
    product = get_object_or_404(
        Product.objects.select_related('category').prefetch_related('images'),
        slug=slug,
        is_active=True
    )
    return product


@router.post("/products", response={201: ProductDetailSchema}, auth=AuthBearer())
def create_product(request, payload: ProductCreateSchema):
    """Create a new product (admin only)"""
    product = Product.objects.create(**payload.dict())
    return 201, product


@router.put("/products/{product_id}", response=ProductDetailSchema, auth=AuthBearer())
def update_product(request, product_id: int, payload: dict):
    """Update product (admin only)"""
    product = get_object_or_404(Product, id=product_id)
    
    for key, value in payload.items():
        setattr(product, key, value)
    
    product.save()
    return product


@router.delete("/products/{product_id}", auth=AuthBearer())
def delete_product(request, product_id: int):
    """Delete product (admin only)"""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"message": "Product deleted successfully"}


# Review endpoints
@router.get("/products/{product_id}/reviews", response=List[ReviewSchema])
def get_product_reviews(request, product_id: int):
    """Get all reviews for a product"""
    reviews = Review.objects.filter(product_id=product_id).select_related('user')
    return [{
        "id": review.id,
        "user_id": review.user.id,
        "username": review.user.username,
        "rating": review.rating,
        "comment": review.comment,
        "created_at": review.created_at
    } for review in reviews]


@router.post("/reviews", response={201: ReviewSchema}, auth=AuthBearer())
def create_review(request, payload: ReviewCreateSchema):
    """Create a product review"""
    user = request.auth
    product = get_object_or_404(Product, id=payload.product_id)
    
    review, created = Review.objects.update_or_create(
        product=product,
        user=user,
        defaults={
            'rating': payload.rating,
            'comment': payload.comment
        }
    )
    
    return 201, {
        "id": review.id,
        "user_id": user.id,
        "username": user.username,
        "rating": review.rating,
        "comment": review.comment,
        "created_at": review.created_at
    }


# Wishlist endpoints
@router.get("/wishlist", response=List[WishlistSchema], auth=AuthBearer())
def get_wishlist(request):
    """Get user's wishlist"""
    wishlist_items = Wishlist.objects.filter(user=request.auth).select_related('product__category')
    return wishlist_items


@router.post("/wishlist", response={201: WishlistSchema}, auth=AuthBearer())
def add_to_wishlist(request, payload: WishlistAddSchema):
    """Add product to wishlist"""
    user = request.auth
    product = get_object_or_404(Product, id=payload.product_id)
    
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=user,
        product=product
    )
    
    return 201, wishlist_item


@router.delete("/wishlist/{product_id}", auth=AuthBearer())
def remove_from_wishlist(request, product_id: int):
    """Remove product from wishlist"""
    wishlist_item = get_object_or_404(Wishlist, user=request.auth, product_id=product_id)
    wishlist_item.delete()
    return {"message": "Product removed from wishlist"}

