# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Activate Virtual Environment

**Option A - PowerShell:**
```powershell
.\activate.ps1
```

**Option B - CMD:**
```cmd
activate.bat
```

**Option C - Manual:**
```bash
.\venv\Scripts\activate
```

### Step 2: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts:
- Username: `admin` (or your choice)
- Email: your email
- Password: create a strong password

### Step 3: Populate Sample Data (Optional)

```bash
python manage.py populate_data
```

This will create:
- 5 categories (Electronics, Clothing, Books, Home & Kitchen, Sports)
- 8 sample products with pricing and stock

### Step 4: Run the Server

```bash
python manage.py runserver
```

### Step 5: Test the API

#### 🌐 Web Browser

1. **Admin Panel**: http://localhost:8000/admin
   - Login with your superuser credentials
   - Add/edit categories and products

2. **API Documentation**: http://localhost:8000/api/docs
   - Interactive Swagger UI
   - Test all endpoints directly

3. **Alternative Docs**: http://localhost:8000/api/redoc
   - Clean ReDoc interface

#### 🧪 Testing with cURL or Postman

**1. Register a User:**
```bash
curl -X POST http://localhost:8000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "phone": "1234567890",
    "address": "123 Test Street"
  }'
```

**2. Login:**
```bash
curl -X POST http://localhost:8000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

Save the `access` token from the response.

**3. Get Products:**
```bash
curl http://localhost:8000/api/products/products
```

**4. Get User Profile (Authenticated):**
```bash
curl http://localhost:8000/api/users/me \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**5. Add to Cart (Authenticated):**
```bash
curl -X POST http://localhost:8000/api/orders/cart \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "quantity": 2
  }'
```

## 📚 All Available Endpoints

Visit: http://localhost:8000/api/docs for complete documentation

## 🎨 Connect Frontend

Your Next.js frontend is at: `../frontend`

### Update Frontend API Base URL

In your Next.js app, set the API base URL:

```typescript
// frontend/lib/api.ts or similar
const API_BASE_URL = 'http://localhost:8000/api';

export const api = {
  async login(username: string, password: string) {
    const response = await fetch(`${API_BASE_URL}/users/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    return response.json();
  },
  
  async getProducts() {
    const response = await fetch(`${API_BASE_URL}/products/products`);
    return response.json();
  },
  
  // Add more API calls as needed
};
```

## 🔥 Pro Tips

1. **Use the Swagger UI** at `/api/docs` for easy testing
2. **Check Django Admin** to manage data visually
3. **JWT tokens expire** - Handle refresh logic in your frontend
4. **CORS is configured** for localhost:3000 (your Next.js app)
5. **Media files** are stored in `/media` directory

## 🛠️ Troubleshooting

### Virtual environment not activating?
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Port 8000 already in use?
```bash
python manage.py runserver 8001
```

### Migration errors?
```bash
python manage.py migrate --run-syncdb
```

### Need to reset database?
```bash
# Delete db.sqlite3 file
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_data
```

## 📞 Need Help?

Check the main README.md for detailed documentation or explore the code - it's well-commented!

---

**You're all set! Happy coding! 🎉**
