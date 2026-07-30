# E-Commerce Backend API with Django Ninja

A complete, production-ready e-commerce backend API built with Django Ninja (preferred by many companies over DRF).

## 🚀 Features

### User Management
- User registration and authentication with JWT
- User profile management
- Custom user model with phone and address fields

### Product Management
- Categories with images
- Products with multiple images
- Product reviews and ratings
- Wishlist functionality
- Stock management
- Featured products
- Discount pricing

### Order Management
- Shopping cart functionality
- Order creation and tracking
- Order status management
- Stock updates on order placement
- Order cancellation with stock restoration

### Payment Processing
- Multiple payment methods (Card, UPI, Net Banking, Wallet, COD)
- Payment status tracking
- Transaction management
- Payment gateway integration ready

## 📦 Tech Stack

- **Django 5.1.5** - Web framework
- **Django Ninja 1.6.2** - Modern API framework
- **Django Ninja JWT** - JWT authentication
- **Pydantic** - Data validation
- **Pillow** - Image processing
- **Django CORS Headers** - CORS support for frontend
- **SQLite** - Database (easily switchable to PostgreSQL/MySQL)

## 🛠️ Installation

### 1. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\activate.ps1
```

**Windows (CMD):**
```cmd
activate.bat
```

**Manual Activation:**
```bash
.\venv\Scripts\activate
```

### 2. Environment Setup

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### 3. Run Migrations (Already Done!)

The migrations have been created and applied. If you need to run them again:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://localhost:8000`

## 📚 API Documentation

Django Ninja provides interactive API documentation:

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI Schema**: http://localhost:8000/api/openapi.json

## 🔑 API Endpoints

### Authentication
- `POST /api/users/register` - Register new user
- `POST /api/users/login` - Login user
- `GET /api/users/me` - Get current user (requires auth)
- `PUT /api/users/me` - Update user profile (requires auth)

### Categories
- `GET /api/products/categories` - List all categories
- `GET /api/products/categories/{slug}` - Get category by slug
- `POST /api/products/categories` - Create category (admin)

### Products
- `GET /api/products/products` - List products (with filters)
- `GET /api/products/products/{slug}` - Get product details
- `POST /api/products/products` - Create product (admin)
- `PUT /api/products/products/{id}` - Update product (admin)
- `DELETE /api/products/products/{id}` - Delete product (admin)

### Reviews
- `GET /api/products/products/{id}/reviews` - Get product reviews
- `POST /api/products/reviews` - Create review (requires auth)

### Wishlist
- `GET /api/products/wishlist` - Get user wishlist (requires auth)
- `POST /api/products/wishlist` - Add to wishlist (requires auth)
- `DELETE /api/products/wishlist/{id}` - Remove from wishlist (requires auth)

### Cart
- `GET /api/orders/cart` - Get cart (requires auth)
- `POST /api/orders/cart` - Add to cart (requires auth)
- `PUT /api/orders/cart/{id}` - Update cart item (requires auth)
- `DELETE /api/orders/cart/{id}` - Remove from cart (requires auth)
- `DELETE /api/orders/cart` - Clear cart (requires auth)

### Orders
- `GET /api/orders/orders` - List user orders (requires auth)
- `GET /api/orders/orders/{id}` - Get order details (requires auth)
- `POST /api/orders/orders` - Create order from cart (requires auth)
- `PATCH /api/orders/orders/{id}` - Update order status (admin)
- `DELETE /api/orders/orders/{id}` - Cancel order (requires auth)

### Payments
- `GET /api/payments/payments` - List user payments (requires auth)
- `GET /api/payments/payments/{id}` - Get payment details (requires auth)
- `POST /api/payments/payments` - Create payment (requires auth)
- `PATCH /api/payments/payments/{id}` - Update payment status (requires auth)
- `POST /api/payments/payments/{id}/verify` - Verify payment (requires auth)

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication.

### Getting Tokens

```bash
curl -X POST http://localhost:8000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using Tokens

Include the access token in the Authorization header:

```bash
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

## 📁 Project Structure

```
backend_Ecommerce/
├── backend_Ecommerce/      # Main project settings
│   ├── settings.py         # Django settings with Ninja config
│   └── urls.py            # Main URL configuration
├── users/                 # User management app
│   ├── models.py         # Custom User model
│   ├── schemas.py        # Pydantic schemas
│   └── views.py          # API endpoints (Router)
├── products/             # Product management app
│   ├── models.py        # Category, Product, Review, Wishlist
│   ├── schemas.py       # Pydantic schemas
│   └── views.py         # API endpoints (Router)
├── orders/              # Order management app
│   ├── models.py       # Cart, Order, OrderItem
│   ├── schemas.py      # Pydantic schemas
│   └── views.py        # API endpoints (Router)
├── payments/           # Payment management app
│   ├── models.py      # Payment model
│   ├── schemas.py     # Pydantic schemas
│   └── views.py       # API endpoints (Router)
├── venv/             # Virtual environment
├── media/            # Uploaded files
├── requirements.txt  # Python dependencies
└── manage.py        # Django management script
```

## 🎨 Frontend Integration

This backend is ready to be integrated with your Next.js frontend.

### CORS Configuration

CORS is already configured for:
- `http://localhost:3000`
- `http://127.0.0.1:3000`

To add more origins, update `CORS_ALLOWED_ORIGINS` in `settings.py`.

### Example Frontend API Call

```typescript
// Login example
const response = await fetch('http://localhost:8000/api/users/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: 'testuser',
    password: 'password123'
  })
});

const data = await response.json();
localStorage.setItem('access_token', data.access);

// Authenticated request
const products = await fetch('http://localhost:8000/api/products/products', {
  headers: {
    'Authorization': `Bearer ${localStorage.getItem('access_token')}`
  }
});
```

## 🧪 Testing

Create some test data through Django admin:

1. Go to http://localhost:8000/admin
2. Login with your superuser credentials
3. Add categories, products, etc.

## 🚀 Why Django Ninja?

1. **Modern & Fast**: Built on Pydantic and type hints
2. **Better Performance**: Faster than DRF in benchmarks
3. **Auto Documentation**: Swagger/OpenAPI out of the box
4. **Type Safety**: Full IDE support with type hints
5. **Less Boilerplate**: Cleaner, more readable code
6. **Industry Adoption**: Growing preference among companies

## 📝 Next Steps

1. **Add Product Data**: Use Django admin to add categories and products
2. **Test API**: Use the Swagger UI at `/api/docs`
3. **Integrate Frontend**: Connect your Next.js app
4. **Payment Gateway**: Integrate Razorpay/Stripe for real payments
5. **Deploy**: Deploy to production (Heroku, AWS, DigitalOcean)

## 🔧 Common Commands

```bash
# Activate virtual environment
.\venv\Scripts\activate

# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

## 📄 License

This project is open source and available for your use.

## 🤝 Support

For issues or questions, please check the API documentation at `/api/docs` or review the code comments.

---

**Happy Coding! 🎉**
