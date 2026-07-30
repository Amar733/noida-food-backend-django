# API Usage Examples

Complete examples for testing your Django Ninja E-Commerce API.

## 🌐 Base URL

```
http://localhost:8000/api
```

## 📝 Interactive Testing

The easiest way to test: **http://localhost:8000/api/docs**

## 🧪 Manual Testing Examples

### 1. User Registration

```bash
curl -X POST http://localhost:8000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepass123",
    "phone": "9876543210",
    "address": "123 Main St, New Delhi"
  }'
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 2. User Login

```bash
curl -X POST http://localhost:8000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepass123"
  }'
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Save the access token for authenticated requests!**

### 3. Get Current User Profile

```bash
curl -X GET http://localhost:8000/api/users/me \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "phone": "9876543210",
  "address": "123 Main St, New Delhi",
  "first_name": "",
  "last_name": "",
  "date_joined": "2026-07-31T00:00:00Z"
}
```

### 4. Update User Profile

```bash
curl -X PUT http://localhost:8000/api/users/me \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "phone": "9876543210",
    "address": "456 New Address, Mumbai"
  }'
```

### 5. Get All Categories

```bash
curl -X GET http://localhost:8000/api/products/categories
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Electronics",
    "slug": "electronics",
    "description": "Electronic devices and accessories",
    "image": null,
    "is_active": true
  }
]
```

### 6. Get Products

```bash
# All products
curl -X GET http://localhost:8000/api/products/products

# Filter by category
curl -X GET "http://localhost:8000/api/products/products?category=electronics"

# Search products
curl -X GET "http://localhost:8000/api/products/products?search=headphones"

# Featured products only
curl -X GET "http://localhost:8000/api/products/products?is_featured=true"
```

**Response:**
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
      "image": null,
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
  "count": 1
}
```

### 7. Get Product Details

```bash
curl -X GET http://localhost:8000/api/products/products/wireless-headphones
```

### 8. Add to Cart

```bash
curl -X POST http://localhost:8000/api/orders/cart \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "quantity": 2
  }'
```

**Response:**
```json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "product_id": 1,
      "product_name": "Wireless Headphones",
      "product_image": null,
      "price": "2999.00",
      "quantity": 2,
      "subtotal": "5998.00"
    }
  ],
  "total": "5998.00",
  "items_count": 2
}
```

### 9. View Cart

```bash
curl -X GET http://localhost:8000/api/orders/cart \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 10. Update Cart Item

```bash
curl -X PUT http://localhost:8000/api/orders/cart/1 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "quantity": 3
  }'
```

### 11. Remove from Cart

```bash
curl -X DELETE http://localhost:8000/api/orders/cart/1 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 12. Clear Cart

```bash
curl -X DELETE http://localhost:8000/api/orders/cart \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 13. Create Order

```bash
curl -X POST http://localhost:8000/api/orders/orders \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "shipping_address": "123 Main Street, Apartment 4B",
    "shipping_city": "New Delhi",
    "shipping_state": "Delhi",
    "shipping_zip": "110001",
    "shipping_phone": "9876543210",
    "notes": "Please call before delivery"
  }'
```

**Response:**
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

### 14. View Orders

```bash
curl -X GET http://localhost:8000/api/orders/orders \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 15. Get Order Details

```bash
curl -X GET http://localhost:8000/api/orders/orders/1 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 16. Cancel Order

```bash
curl -X DELETE http://localhost:8000/api/orders/orders/1 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 17. Create Payment

```bash
curl -X POST http://localhost:8000/api/payments/payments \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": 1,
    "payment_method": "upi",
    "transaction_id": "TXN123456789",
    "payment_gateway": "razorpay"
  }'
```

### 18. Update Payment Status

```bash
curl -X PATCH http://localhost:8000/api/payments/payments/1 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "completed",
    "transaction_id": "TXN123456789"
  }'
```

### 19. Add Product Review

```bash
curl -X POST http://localhost:8000/api/products/reviews \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "rating": 5,
    "comment": "Excellent product! Highly recommended."
  }'
```

### 20. Get Product Reviews

```bash
curl -X GET http://localhost:8000/api/products/products/1/reviews
```

### 21. Add to Wishlist

```bash
curl -X POST http://localhost:8000/api/products/wishlist \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1
  }'
```

### 22. View Wishlist

```bash
curl -X GET http://localhost:8000/api/products/wishlist \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 23. Remove from Wishlist

```bash
curl -X DELETE http://localhost:8000/api/products/wishlist/1 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🎨 Frontend JavaScript/TypeScript Examples

### Setup API Client

```typescript
// lib/api.ts
const API_BASE_URL = 'http://localhost:8000/api';

class ApiClient {
  private getAuthHeaders(): HeadersInit {
    const token = localStorage.getItem('access_token');
    return {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` })
    };
  }

  async register(data: {
    username: string;
    email: string;
    password: string;
    phone?: string;
    address?: string;
  }) {
    const response = await fetch(`${API_BASE_URL}/users/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    const result = await response.json();
    if (response.ok) {
      localStorage.setItem('access_token', result.access);
      localStorage.setItem('refresh_token', result.refresh);
    }
    return result;
  }

  async login(username: string, password: string) {
    const response = await fetch(`${API_BASE_URL}/users/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const result = await response.json();
    if (response.ok) {
      localStorage.setItem('access_token', result.access);
      localStorage.setItem('refresh_token', result.refresh);
    }
    return result;
  }

  async getProducts(filters?: {
    category?: string;
    search?: string;
    is_featured?: boolean;
  }) {
    const params = new URLSearchParams(filters as any);
    const response = await fetch(
      `${API_BASE_URL}/products/products?${params}`
    );
    return response.json();
  }

  async getProduct(slug: string) {
    const response = await fetch(
      `${API_BASE_URL}/products/products/${slug}`
    );
    return response.json();
  }

  async addToCart(productId: number, quantity: number = 1) {
    const response = await fetch(`${API_BASE_URL}/orders/cart`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify({ product_id: productId, quantity })
    });
    return response.json();
  }

  async getCart() {
    const response = await fetch(`${API_BASE_URL}/orders/cart`, {
      headers: this.getAuthHeaders()
    });
    return response.json();
  }

  async createOrder(data: {
    shipping_address: string;
    shipping_city: string;
    shipping_state: string;
    shipping_zip: string;
    shipping_phone: string;
    notes?: string;
  }) {
    const response = await fetch(`${API_BASE_URL}/orders/orders`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(data)
    });
    return response.json();
  }

  async getOrders() {
    const response = await fetch(`${API_BASE_URL}/orders/orders`, {
      headers: this.getAuthHeaders()
    });
    return response.json();
  }
}

export const api = new ApiClient();
```

### Usage in Components

```typescript
// Example: Product List Component
import { api } from '@/lib/api';
import { useEffect, useState } from 'react';

export default function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.getProducts().then(data => setProducts(data.items));
  }, []);

  return (
    <div>
      {products.map(product => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>₹{product.price}</p>
          <button onClick={() => api.addToCart(product.id, 1)}>
            Add to Cart
          </button>
        </div>
      ))}
    </div>
  );
}
```

## 🔒 Authentication Flow

1. User registers/logs in
2. Store `access` and `refresh` tokens
3. Include `Authorization: Bearer {access_token}` in all authenticated requests
4. When access token expires, use refresh token to get a new one
5. If refresh token expires, user must log in again

## ✅ Testing Checklist

- [ ] User registration works
- [ ] User login returns tokens
- [ ] Can access protected endpoints with token
- [ ] Can browse products
- [ ] Can add products to cart
- [ ] Can create orders
- [ ] Can process payments
- [ ] Can add reviews
- [ ] Wishlist functionality works

---

**Use the Swagger UI at http://localhost:8000/api/docs for the easiest testing experience!**
