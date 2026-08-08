# API Endpoints Documentation

Complete list of all available API endpoints organized by category.

**Base URL:** `http://localhost:8000/api`

**Interactive Documentation:** http://localhost:8000/api/docs

---

## 📋 Table of Contents

1. [Authentication](#authentication)
2. [User Management](#user-management)
3. [Categories](#categories)
4. [Products](#products)
5. [Reviews](#reviews)
6. [Wishlist](#wishlist)
7. [Shopping Cart](#shopping-cart)
8. [Orders](#orders)
9. [Payments](#payments)

---

## 🔐 Authentication

### Register New User
```
POST /api/users/register
```

**Request Body:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepass123",
  "phone": "9876543210",
  "address": "123 Main St, New Delhi"
}
```

**Response:** `201 Created`
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Error Response:** `400 Bad Request`
```json
{
  "error": "Username already taken"
}
```

---

### Login User
```
POST /api/users/login
```

**Request Body:**
```json
{
  "username": "john_doe",
  "password": "securepass123"
}
```

**Response:** `200 OK`
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Error Response:** `401 Unauthorized`
```json
{
  "error": "Invalid credentials"
}
```

---

## 👤 User Management

### Get Current User Profile
```
GET /api/users/me
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "phone": "9876543210",
  "address": "123 Main St, New Delhi",
  "first_name": "John",
  "last_name": "Doe",
  "date_joined": "2026-07-31T00:00:00Z"
}
```

---

### Update User Profile
```
PUT /api/users/me
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "phone": "9876543210",
  "address": "456 New Address, Mumbai",
  "email": "newemail@example.com"
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "newemail@example.com",
  "phone": "9876543210",
  "address": "456 New Address, Mumbai",
  "first_name": "John",
  "last_name": "Doe",
  "date_joined": "2026-07-31T00:00:00Z"
}
```

---

## 📂 Categories

### List All Categories
```
GET /api/products/categories
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "name": "Electronics",
    "slug": "electronics",
    "description": "Electronic devices and accessories",
    "image": "/media/categories/electronics.jpg",
    "is_active": true
  },
  {
    "id": 2,
    "name": "Clothing",
    "slug": "clothing",
    "description": "Fashion and apparel",
    "image": null,
    "is_active": true
  }
]
```

---

### Get Category by Slug
```
GET /api/products/categories/{slug}
```

**Example:** `/api/products/categories/electronics`

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "Electronics",
  "slug": "electronics",
  "description": "Electronic devices and accessories",
  "image": "/media/categories/electronics.jpg",
  "is_active": true
}
```

**Error Response:** `404 Not Found`

---

### Create Category (Admin Only)
```
POST /api/products/categories
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "name": "Gaming",
  "slug": "gaming",
  "description": "Gaming consoles and accessories",
  "is_active": true
}
```

**Response:** `201 Created`
```json
{
  "id": 6,
  "name": "Gaming",
  "slug": "gaming",
  "description": "Gaming consoles and accessories",
  "image": null,
  "is_active": true
}
```

---

## 🛍️ Products

### List All Products
```
GET /api/products/products
```

**Query Parameters:**
- `category` (string) - Filter by category slug (e.g., `?category=electronics`)
- `is_featured` (boolean) - Filter featured products (e.g., `?is_featured=true`)
- `search` (string) - Search products by name (e.g., `?search=headphones`)

**Examples:**
- All products: `/api/products/products`
- Electronics only: `/api/products/products?category=electronics`
- Featured products: `/api/products/products?is_featured=true`
- Search: `/api/products/products?search=wireless`

**Response:** `200 OK`
```json
{
  "items": [
    {
      "id": 1,
      "name": "Wireless Headphones",
      "slug": "wireless-headphones",
      "price": "2999.00",
      "compare_price": "4999.00",
      "stock": 50,
      "image": "/media/products/headphones.jpg",
      "is_featured": true,
      "discount_percentage": 40,
      "category": {
        "id": 1,
        "name": "Electronics",
        "slug": "electronics",
        "description": "Electronic devices",
        "image": null,
        "is_active": true
      }
    }
  ],
  "count": 8
}
```

---

### Get Product Details by Slug
```
GET /api/products/products/{slug}
```

**Example:** `/api/products/products/wireless-headphones`

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "Wireless Headphones",
  "slug": "wireless-headphones",
  "description": "High-quality wireless headphones with noise cancellation",
  "price": "2999.00",
  "compare_price": "4999.00",
  "stock": 50,
  "image": "/media/products/headphones.jpg",
  "is_active": true,
  "is_featured": true,
  "discount_percentage": 40,
  "category": {
    "id": 1,
    "name": "Electronics",
    "slug": "electronics",
    "description": "Electronic devices and accessories",
    "image": null,
    "is_active": true
  },
  "images": [
    {
      "id": 1,
      "image": "/media/products/gallery/headphones_1.jpg",
      "alt_text": "Front view",
      "is_primary": true
    }
  ],
  "created_at": "2026-07-31T00:00:00Z",
  "updated_at": "2026-07-31T00:00:00Z"
}
```

**Error Response:** `404 Not Found`

---

### Create Product (Admin Only)
```
POST /api/products/products
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "category_id": 1,
  "name": "Laptop Stand",
  "slug": "laptop-stand",
  "description": "Adjustable aluminum laptop stand",
  "price": "1499.00",
  "compare_price": "2499.00",
  "stock": 100,
  "is_active": true,
  "is_featured": false
}
```

**Response:** `201 Created`

---

### Update Product (Admin Only)
```
PUT /api/products/products/{product_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "price": "2499.00",
  "stock": 75,
  "is_featured": true
}
```

**Response:** `200 OK`

---

### Delete Product (Admin Only)
```
DELETE /api/products/products/{product_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "message": "Product deleted successfully"
}
```

---

## ⭐ Reviews

### Get Product Reviews
```
GET /api/products/products/{product_id}/reviews
```

**Example:** `/api/products/products/1/reviews`

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "user_id": 2,
    "username": "jane_doe",
    "rating": 5,
    "comment": "Excellent product! Highly recommended.",
    "created_at": "2026-07-31T00:00:00Z"
  },
  {
    "id": 2,
    "user_id": 3,
    "username": "bob_smith",
    "rating": 4,
    "comment": "Good quality, worth the price.",
    "created_at": "2026-07-30T00:00:00Z"
  }
]
```

---

### Create/Update Product Review
```
POST /api/products/reviews
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "product_id": 1,
  "rating": 5,
  "comment": "Amazing product! Very satisfied with the purchase."
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "user_id": 1,
  "username": "john_doe",
  "rating": 5,
  "comment": "Amazing product! Very satisfied with the purchase.",
  "created_at": "2026-07-31T00:00:00Z"
}
```

**Note:** If user already reviewed this product, it will update the existing review.

---

## 💝 Wishlist

### Get User Wishlist
```
GET /api/products/wishlist
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "product": {
      "id": 2,
      "name": "Smart Watch",
      "slug": "smart-watch",
      "price": "5999.00",
      "compare_price": "8999.00",
      "stock": 30,
      "image": "/media/products/smartwatch.jpg",
      "is_featured": true,
      "discount_percentage": 33,
      "category": {
        "id": 1,
        "name": "Electronics",
        "slug": "electronics",
        "description": "Electronic devices",
        "image": null,
        "is_active": true
      }
    },
    "created_at": "2026-07-31T00:00:00Z"
  }
]
```

---

### Add Product to Wishlist
```
POST /api/products/wishlist
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "product_id": 2
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "product": {
    "id": 2,
    "name": "Smart Watch",
    "slug": "smart-watch",
    "price": "5999.00",
    "compare_price": "8999.00",
    "stock": 30,
    "image": "/media/products/smartwatch.jpg",
    "is_featured": true,
    "discount_percentage": 33,
    "category": {
      "id": 1,
      "name": "Electronics",
      "slug": "electronics",
      "description": "Electronic devices",
      "image": null,
      "is_active": true
    }
  },
  "created_at": "2026-07-31T00:00:00Z"
}
```

---

### Remove Product from Wishlist
```
DELETE /api/products/wishlist/{product_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "message": "Product removed from wishlist"
}
```

---

## 🛒 Shopping Cart

### View Cart
```
GET /api/orders/cart
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "product_id": 1,
      "product_name": "Wireless Headphones",
      "product_image": "/media/products/headphones.jpg",
      "price": "2999.00",
      "quantity": 2,
      "subtotal": "5998.00"
    },
    {
      "id": 2,
      "product_id": 3,
      "product_name": "Bluetooth Speaker",
      "product_image": "/media/products/speaker.jpg",
      "price": "1999.00",
      "quantity": 1,
      "subtotal": "1999.00"
    }
  ],
  "total": "7997.00",
  "items_count": 3
}
```

---

### Add Item to Cart
```
POST /api/orders/cart
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "product_id": 1,
  "quantity": 2
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "product_id": 1,
      "product_name": "Wireless Headphones",
      "product_image": "/media/products/headphones.jpg",
      "price": "2999.00",
      "quantity": 2,
      "subtotal": "5998.00"
    }
  ],
  "total": "5998.00",
  "items_count": 2
}
```

**Error Response:** `400 Bad Request`
```json
{
  "error": "Insufficient stock"
}
```

---

### Update Cart Item Quantity
```
PUT /api/orders/cart/{item_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "quantity": 3
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "product_id": 1,
      "product_name": "Wireless Headphones",
      "product_image": "/media/products/headphones.jpg",
      "price": "2999.00",
      "quantity": 3,
      "subtotal": "8997.00"
    }
  ],
  "total": "8997.00",
  "items_count": 3
}
```

---

### Remove Item from Cart
```
DELETE /api/orders/cart/{item_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "message": "Item removed from cart"
}
```

---

### Clear Entire Cart
```
DELETE /api/orders/cart
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "message": "Cart cleared"
}
```

---

## 📦 Orders

### List User Orders
```
GET /api/orders/orders
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "order_number": "ORD-A1B2C3D4",
    "total_amount": "5998.00",
    "status": "pending",
    "created_at": "2026-07-31T00:00:00Z"
  },
  {
    "id": 2,
    "order_number": "ORD-X9Y8Z7W6",
    "total_amount": "1299.00",
    "status": "delivered",
    "created_at": "2026-07-25T00:00:00Z"
  }
]
```

---

### Get Order Details
```
GET /api/orders/orders/{order_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "order_number": "ORD-A1B2C3D4",
  "total_amount": "5998.00",
  "status": "pending",
  "shipping_address": "123 Main Street, Apartment 4B",
  "shipping_city": "New Delhi",
  "shipping_state": "Delhi",
  "shipping_zip": "110001",
  "shipping_phone": "9876543210",
  "tracking_number": null,
  "items": [
    {
      "id": 1,
      "product_id": 1,
      "product_name": "Wireless Headphones",
      "quantity": 2,
      "price": "2999.00",
      "subtotal": "5998.00"
    }
  ],
  "created_at": "2026-07-31T00:00:00Z",
  "updated_at": "2026-07-31T00:00:00Z"
}
```

---

### Create Order from Cart
```
POST /api/orders/orders
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "shipping_address": "123 Main Street, Apartment 4B",
  "shipping_city": "New Delhi",
  "shipping_state": "Delhi",
  "shipping_zip": "110001",
  "shipping_phone": "9876543210",
  "notes": "Please call before delivery"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "order_number": "ORD-A1B2C3D4",
  "total_amount": "5998.00",
  "status": "pending",
  "shipping_address": "123 Main Street, Apartment 4B",
  "shipping_city": "New Delhi",
  "shipping_state": "Delhi",
  "shipping_zip": "110001",
  "shipping_phone": "9876543210",
  "tracking_number": null,
  "items": [
    {
      "id": 1,
      "product_id": 1,
      "product_name": "Wireless Headphones",
      "quantity": 2,
      "price": "2999.00",
      "subtotal": "5998.00"
    }
  ],
  "created_at": "2026-07-31T00:00:00Z",
  "updated_at": "2026-07-31T00:00:00Z"
}
```

**Error Response:** `400 Bad Request`
```json
{
  "error": "Cart is empty"
}
```

---

### Update Order Status (Admin Only)
```
PATCH /api/orders/orders/{order_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "status": "shipped",
  "tracking_number": "TRK123456789"
}
```

**Valid Status Values:**
- `pending`
- `processing`
- `shipped`
- `delivered`
- `cancelled`

**Response:** `200 OK`

---

### Cancel Order
```
DELETE /api/orders/orders/{order_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "message": "Order cancelled successfully"
}
```

**Error Response:** `400 Bad Request`
```json
{
  "error": "Order cannot be cancelled"
}
```

**Note:** Only orders with status `pending` or `processing` can be cancelled.

---

## 💳 Payments

### List User Payments
```
GET /api/payments/payments
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
[
  {
    "id": 1,
    "order_id": 1,
    "order_number": "ORD-A1B2C3D4",
    "amount": "5998.00",
    "payment_method": "upi",
    "status": "completed",
    "transaction_id": "TXN123456789",
    "payment_gateway": "razorpay",
    "created_at": "2026-07-31T00:00:00Z",
    "updated_at": "2026-07-31T00:00:00Z"
  }
]
```

---

### Get Payment Details
```
GET /api/payments/payments/{payment_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "order_id": 1,
  "order_number": "ORD-A1B2C3D4",
  "amount": "5998.00",
  "payment_method": "upi",
  "status": "completed",
  "transaction_id": "TXN123456789",
  "payment_gateway": "razorpay",
  "created_at": "2026-07-31T00:00:00Z",
  "updated_at": "2026-07-31T00:00:00Z"
}
```

---

### Create Payment
```
POST /api/payments/payments
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "order_id": 1,
  "payment_method": "upi",
  "transaction_id": "TXN123456789",
  "payment_gateway": "razorpay"
}
```

**Payment Methods:**
- `card` - Credit/Debit Card
- `upi` - UPI
- `netbanking` - Net Banking
- `wallet` - Wallet
- `cod` - Cash on Delivery

**Response:** `201 Created`
```json
{
  "id": 1,
  "order_id": 1,
  "order_number": "ORD-A1B2C3D4",
  "amount": "5998.00",
  "payment_method": "upi",
  "status": "pending",
  "transaction_id": "TXN123456789",
  "payment_gateway": "razorpay",
  "created_at": "2026-07-31T00:00:00Z",
  "updated_at": "2026-07-31T00:00:00Z"
}
```

**Error Response:** `400 Bad Request`
```json
{
  "error": "Payment already exists for this order"
}
```

---

### Update Payment Status
```
PATCH /api/payments/payments/{payment_id}
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "status": "completed",
  "transaction_id": "TXN123456789"
}
```

**Valid Status Values:**
- `pending`
- `completed`
- `failed`
- `refunded`

**Response:** `200 OK`

**Note:** When payment status is set to `completed`, the order status is automatically updated to `processing`.

---

### Verify Payment
```
POST /api/payments/payments/{payment_id}/verify
```

**Headers:**
```
Authorization: Bearer {access_token}
Content-Type: application/json
```

**Request Body:**
```json
{
  "razorpay_payment_id": "pay_123456789",
  "razorpay_order_id": "order_987654321",
  "razorpay_signature": "signature_hash_here"
}
```

**Response:** `200 OK`
```json
{
  "message": "Payment verified successfully",
  "payment": {
    "id": 1,
    "order_id": 1,
    "order_number": "ORD-A1B2C3D4",
    "amount": "5998.00",
    "payment_method": "upi",
    "status": "completed",
    "transaction_id": "TXN123456789",
    "payment_gateway": "razorpay",
    "created_at": "2026-07-31T00:00:00Z",
    "updated_at": "2026-07-31T00:00:00Z"
  }
}
```

---

## 📊 Summary

### Endpoint Count by Category

| Category | Endpoints | Auth Required |
|----------|-----------|---------------|
| Authentication | 2 | No |
| User Management | 2 | Yes |
| Categories | 3 | Mixed |
| Products | 6 | Mixed |
| Reviews | 2 | Mixed |
| Wishlist | 3 | Yes |
| Shopping Cart | 5 | Yes |
| Orders | 5 | Yes |
| Payments | 5 | Yes |
| **TOTAL** | **33** | - |

### HTTP Methods Used

- `GET` - Retrieve data (18 endpoints)
- `POST` - Create data (10 endpoints)
- `PUT` - Update data (2 endpoints)
- `PATCH` - Partial update (2 endpoints)
- `DELETE` - Delete data (4 endpoints)

---

## 🔑 Authentication Header Format

For all protected endpoints, include the JWT token:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

---

## 🌐 Testing Tools

1. **Swagger UI** (Recommended): http://localhost:8000/api/docs
2. **ReDoc**: http://localhost:8000/api/redoc
3. **Postman**: Import OpenAPI schema from http://localhost:8000/api/openapi.json
4. **cURL**: Use examples provided in API_EXAMPLES.md

---

## 📝 Notes

- All timestamps are in ISO 8601 format (UTC)
- All prices are in INR (Indian Rupees)
- Image URLs are relative to the media root
- Pagination is automatic for list endpoints
- Error responses follow a consistent format with `error` key

---

**For detailed examples and code snippets, see API_EXAMPLES.md**
