from ninja import Router
from ninja.pagination import paginate
from typing import List, Dict, Any
from django.shortcuts import get_object_or_404
from collections import defaultdict
from .models import Category, Product, Review, Wishlist, ProductImage
from .schemas import (
    CategorySchema, CategoryCreateSchema,
    ProductListSchema, ProductDetailSchema, ProductCreateSchema,
    ReviewSchema, ReviewCreateSchema,
    WishlistSchema, WishlistAddSchema,
    ProductItemSchema, SubCategorySchema
)
from users.views import AuthBearer

router = Router()


# Product endpoints
@router.get("/products")
def list_products(request):
    """Get all products organized by categories and sub-categories"""
    # Fetch all active categories and products
    categories = Category.objects.filter(is_active=True).prefetch_related('products')
    
    # Build the response structure
    categories_data = []
    total_items = 0
    
    for category in categories:
        products = category.products.filter(is_active=True)
        
        if not products.exists():
            continue
        
        # Group products by parent category name
        # Determine the grouping strategy based on category name
        category_slug = category.slug
        category_name = category.name.lower()
        
        # Create sub_categories structure
        sub_categories = {}
        
        # For chicken category - group by type
        if 'chicken' in category_slug:
            sub_category_groups = defaultdict(list)
            for product in products:
                product_name_lower = product.name.lower()
                # Categorize based on product name
                if any(word in product_name_lower for word in ['starter', 'appetizer', 'tikka', 'kebab', 'wings']):
                    group_key = 'starters'
                elif any(word in product_name_lower for word in ['curry', 'masala', 'korma', 'vindaloo']):
                    group_key = 'curries'
                elif 'biryani' in product_name_lower:
                    group_key = 'biryani'
                elif any(word in product_name_lower for word in ['tandoori', 'grilled']):
                    group_key = 'tandoori'
                elif any(word in product_name_lower for word in ['chinese', 'manchurian', 'chilli']):
                    group_key = 'chinese'
                elif any(word in product_name_lower for word in ['burger', 'pizza', 'fries', 'sandwich']):
                    group_key = 'fast_food'
                elif any(word in product_name_lower for word in ['roll', 'wrap', 'kathi']):
                    group_key = 'rolls_wraps'
                elif any(word in product_name_lower for word in ['fried', 'crispy']):
                    group_key = 'fried_chicken'
                elif 'grilled' in product_name_lower:
                    group_key = 'grilled_chicken'
                elif any(word in product_name_lower for word in ['combo', 'meal', 'deal']):
                    group_key = 'combo_meals'
                else:
                    group_key = 'starters'  # default
                
                sub_category_groups[group_key].append(product)
            
            # Create chicken sub_categories structure
            chicken_groups = {}
            for group_key, group_products in sub_category_groups.items():
                chicken_groups[group_key] = [{
                    'id': category.id,
                    'name': category.name,
                    'slug': category.slug,
                    'description': category.description,
                    'image': category.image,
                    'is_active': category.is_active,
                    'items': [
                        {
                            'id': p.id,
                            'name': p.name,
                            'slug': p.slug,
                            'price': str(p.price),
                            'compare_price': str(p.compare_price) if p.compare_price else None,
                            'stock': p.stock,
                            'image': p.image,
                            'is_featured': p.is_featured,
                            'discount_percentage': p.discount_percentage
                        }
                        for p in group_products
                    ]
                }]
            
            sub_categories['chicken'] = chicken_groups
        
        # For sweets category - group by type
        elif 'sweet' in category_slug or 'sweet' in category_name:
            sub_category_groups = defaultdict(list)
            for product in products:
                product_name_lower = product.name.lower()
                # Categorize based on product name
                if 'diwali' in product_name_lower or 'assorted' in product_name_lower:
                    group_key = 'diwali_sweets'
                elif 'barfi' in product_name_lower or 'burfi' in product_name_lower:
                    group_key = 'barfi'
                elif 'laddo' in product_name_lower or 'ladoo' in product_name_lower:
                    group_key = 'laddoo'
                elif 'halwa' in product_name_lower or 'halva' in product_name_lower:
                    group_key = 'halwa'
                elif 'peda' in product_name_lower or 'pera' in product_name_lower:
                    group_key = 'peda'
                elif 'gulab jamun' in product_name_lower:
                    group_key = 'gulab_jamun'
                elif 'rasgulla' in product_name_lower or 'rasmalai' in product_name_lower:
                    group_key = 'rasgulla_rasmalai'
                elif any(word in product_name_lower for word in ['dry fruit', 'dryfruit', 'kaju', 'badam', 'pista']):
                    group_key = 'dry_fruit_sweets'
                elif 'kaju katli' in product_name_lower or 'kaju barfi' in product_name_lower:
                    group_key = 'kaju_katli'
                elif 'jalebi' in product_name_lower or 'imarti' in product_name_lower:
                    group_key = 'jalebi_imarti'
                else:
                    group_key = 'diwali_sweets'  # default
                
                sub_category_groups[group_key].append(product)
            
            # Create sweets sub_categories structure
            sweets_groups = {}
            for group_key, group_products in sub_category_groups.items():
                sweets_groups[group_key] = [{
                    'id': category.id,
                    'name': category.name,
                    'slug': category.slug,
                    'description': category.description,
                    'image': category.image,
                    'is_active': category.is_active,
                    'items': [
                        {
                            'id': p.id,
                            'name': p.name,
                            'slug': p.slug,
                            'price': str(p.price),
                            'compare_price': str(p.compare_price) if p.compare_price else None,
                            'stock': p.stock,
                            'image': p.image,
                            'is_featured': p.is_featured,
                            'discount_percentage': p.discount_percentage
                        }
                        for p in group_products
                    ]
                }]
            
            sub_categories['sweets'] = sweets_groups
        
        # Add category to response
        if sub_categories:
            categories_data.append({
                'id': category.id,
                'name': category.name,
                'slug': category.slug,
                'description': category.description,
                'image': category.image,
                'is_active': category.is_active,
                'sub_categories': sub_categories
            })
            total_items += products.count()
    
    return {
        'status': 'success',
        'message': 'Products retrieved successfully',
        'data': {
            'total_items': total_items,
            'categories': categories_data
        }
    }


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

