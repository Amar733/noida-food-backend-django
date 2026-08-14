# Product Management Tools

This folder contains tools to interact with the Product APIs (Chicken, Dry Fruits, Sweets).

## 📄 Files

1. **product.html** - Interactive web interface (Recommended)
2. **product.py** - Python script for programmatic access

---

## 🌐 Using the HTML Interface (Recommended for Browser)

### Step 1: Start Django Server
```bash
cd backend_Ecommerce
python manage.py runserver
```

### Step 2: Open HTML File
Simply open `product.html` in any web browser (Chrome, Firefox, Edge, etc.)

### Step 3: Configure Settings
- **Base URL**: Usually `http://localhost:8000`
- **Auth Token**: Enter your authentication token (required for POST/PUT/DELETE operations)

### Step 4: Use the Interface
- Click on tabs (🍗 Chicken, 🥜 Dry Fruits, 🍬 Sweets) to switch categories
- Each tab has cards for different operations:
  - **GET** - Retrieve all items
  - **POST** - Create single or multiple items
  - **PUT** - Update existing items
  - **DELETE** - Remove items
- Fill in the forms and click the buttons
- Responses appear below each operation

---

## 🐍 Using the Python Script

### Installation
```bash
pip install requests
```

### Basic Usage
```python
from product import ChickenCRUD

# Initialize with your auth token
crud = ChickenCRUD(
    base_url="http://localhost:8000",
    auth_token="your-auth-token-here"
)

# Get all chicken items
all_items = crud.get_all_chicken_items()
print(all_items)

# Create a single item
new_item = crud.create_chicken_item(
    name="Chicken Biryani",
    price=249,
    image="chicken-biryani.jpg"
)

# Update an item
updated = crud.update_chicken_item(
    item_name="Chicken Biryani",
    price=269
)

# Delete an item
crud.delete_chicken_item("Chicken Biryani")
```

---

## 🔑 Getting an Auth Token

To perform POST, PUT, and DELETE operations, you need an authentication token:

### Option 1: Use Django Admin
1. Go to `http://localhost:8000/admin`
2. Login with your admin credentials
3. Use browser developer tools to extract the session token

### Option 2: Use the Login API
```python
import requests

response = requests.post(
    'http://localhost:8000/users/login',
    json={
        'email': 'your@email.com',
        'password': 'your-password'
    }
)

token = response.json()['token']
print(f"Token: {token}")
```

---

## 📊 API Endpoints

### Chicken Endpoints
- `GET /products/chicken/data` - Get all chicken items
- `POST /products/chicken/data` - Create multiple items (bulk)
- `POST /products/chicken/items` - Create single item
- `PUT /products/chicken/items/{name}` - Update item by name
- `DELETE /products/chicken/items/{name}` - Delete item by name

### Dry Fruits Endpoints (Coming Soon)
- `GET /products/dryfruits/data`
- `POST /products/dryfruits/data`
- `POST /products/dryfruits/items`
- `PUT /products/dryfruits/items/{name}`
- `DELETE /products/dryfruits/items/{name}`

### Sweets Endpoints (Coming Soon)
- `GET /products/sweets/data`
- `POST /products/sweets/data`
- `POST /products/sweets/items`
- `PUT /products/sweets/items/{name}`
- `DELETE /products/sweets/items/{name}`

---

## 🎨 Features of HTML Interface

✅ **Beautiful UI** - Modern gradient design with smooth animations
✅ **Tabbed Navigation** - Easy switching between product categories
✅ **Form Validation** - Prevents invalid submissions
✅ **Real-time Response** - See API responses immediately
✅ **Color-coded Methods** - Visual distinction between GET, POST, PUT, DELETE
✅ **Error Handling** - Clear error messages when something goes wrong
✅ **Responsive Design** - Works on desktop and mobile devices

---

## 🛠️ Troubleshooting

### CORS Issues
If you get CORS errors in the browser, add this to your Django settings:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # For development only
```

### Authentication Errors
- Make sure your auth token is valid
- Check if the token is properly formatted (Bearer token)
- Verify the user has admin permissions

### Connection Refused
- Ensure Django server is running: `python manage.py runserver`
- Check if the Base URL is correct
- Verify no firewall is blocking the connection

---

## 📝 Example Data Format

### Single Item (POST /products/chicken/items)
```json
{
  "name": "Chicken Tikka",
  "price": 199,
  "image": "chicken-tikka.jpg"
}
```

### Bulk Items (POST /products/chicken/data)
```json
{
  "category": "Chicken",
  "items": [
    {"name": "Chicken Tikka", "price": 199, "image": "chicken-tikka.jpg"},
    {"name": "Butter Chicken", "price": 299, "image": "butter-chicken.jpg"},
    {"name": "Chicken Curry", "price": 249, "image": "chicken-curry.jpg"}
  ]
}
```

### Update Item (PUT /products/chicken/items/{name})
```json
{
  "price": 269,
  "image": "new-chicken-biryani.jpg"
}
```

---

## 💡 Tips

1. **Start with GET** - Always test the GET endpoint first to see existing data
2. **Use Single POST** - When adding one item, use the single POST endpoint
3. **Use Bulk POST** - When adding multiple items, use the bulk endpoint
4. **Update Partially** - You don't need to send all fields when updating
5. **Confirm Deletes** - The HTML interface will ask for confirmation before deleting

---

## 🚀 Next Steps

1. Implement similar views for Dry Fruits and Sweets
2. Add image upload functionality
3. Add search and filter capabilities
4. Implement pagination for large datasets
5. Add export/import functionality

---

**Enjoy managing your products! 🎉**
