# How to Add More Products with Images

## Quick Guide for Adding New Products to Your Database

---

## Method 1: Using the populate_data.py Script

### Step 1: Edit the Script
Open `products/management/commands/populate_data.py`

### Step 2: Add New Product Entry
Add your product to the `products_data` list:

```python
{
    'category': 'chicken-starters',  # Use existing category slug
    'name': 'Chicken Pakora Supreme',
    'slug': 'chicken-pakora-supreme',  # Must be unique
    'description': 'Extra crispy chicken pakoras with special spices',
    'price': Decimal('279.00'),
    'compare_price': Decimal('329.00'),  # Optional
    'stock': 50,
    'is_featured': True,  # or False
    'image': 'https://images.unsplash.com/photo-XXXXXX?w=800&q=80'  # ← Important!
},
```

### Step 3: Find Food Images

#### Option A: Unsplash
1. Go to https://unsplash.com
2. Search for your food (e.g., "chicken pakora", "fried chicken")
3. Click on an image
4. Right-click → Copy image URL
5. Add parameters: `?w=800&q=80`
6. Example: `https://images.unsplash.com/photo-1234567890?w=800&q=80`

#### Option B: Pexels
1. Go to https://pexels.com
2. Search for your food
3. Click on an image
4. Click "Download" → Copy URL
5. Add parameters: `?auto=compress&cs=tinysrgb&w=800`
6. Example: `https://images.pexels.com/photos/1234567/pexels-photo-1234567.jpeg?auto=compress&cs=tinysrgb&w=800`

#### Option C: Pixabay
1. Go to https://pixabay.com
2. Search and get image URL
3. Use similar optimization parameters

### Step 4: Run the Command
```bash
python manage.py populate_data
```

**Note**: This will only add new products (won't duplicate existing ones due to `get_or_create`)

---

## Method 2: Using Django Admin Panel

### Step 1: Create a Superuser (if not done)
```bash
python manage.py createsuperuser
```

### Step 2: Access Admin Panel
```
http://localhost:8000/admin
```

### Step 3: Add Product
1. Login with superuser credentials
2. Click "Products" → "Add Product"
3. Fill in all fields:
   - Name
   - Slug (auto-generated from name)
   - Description
   - Price
   - Category (select from dropdown)
   - **Image URL** (paste from Unsplash/Pexels)
   - Stock
   - Is Featured (checkbox)
4. Click "Save"

---

## Method 3: Using Python Shell

### Step 1: Open Shell
```bash
python manage.py shell
```

### Step 2: Create Product
```python
from products.models import Product, Category
from decimal import Decimal

# Get category
category = Category.objects.get(slug='chicken-starters')

# Create product
product = Product.objects.create(
    name='Chicken Pakora Supreme',
    slug='chicken-pakora-supreme',
    description='Extra crispy chicken pakoras',
    price=Decimal('279.00'),
    compare_price=Decimal('329.00'),
    stock=50,
    is_featured=True,
    category=category,
    image='https://images.unsplash.com/photo-XXXXXX?w=800&q=80'
)

print(f"Created: {product.name}")
```

---

## Method 4: Using API (If you have POST enabled)

### Step 1: Send POST Request
```bash
curl -X POST http://localhost:8000/api/products/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Chicken Pakora Supreme",
    "slug": "chicken-pakora-supreme",
    "description": "Extra crispy chicken pakoras",
    "price": "279.00",
    "compare_price": "329.00",
    "stock": 50,
    "is_featured": true,
    "category": 1,
    "image": "https://images.unsplash.com/photo-XXXXXX?w=800&q=80"
  }'
```

---

## Image URL Guidelines

### Best Practices
✅ **Always use HTTPS** (not HTTP)  
✅ **Add optimization parameters** (`w=800&q=80`)  
✅ **Use CDN sources** (Unsplash, Pexels, Pixabay)  
✅ **Choose high-quality images** (min 800px width)  
✅ **Select relevant images** (matches product description)

### URL Format Examples

#### Unsplash
```
https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800&q=80
```

#### Pexels
```
https://images.pexels.com/photos/60616/fried-chicken-chicken-fried-crunchy-60616.jpeg?auto=compress&cs=tinysrgb&w=800
```

#### Pixabay
```
https://pixabay.com/get/[image-id].jpg?w=800
```

---

## Adding a New Category

### Step 1: Add Category to Script
In `populate_data.py`, add to `categories_data`:

```python
{
    'name': 'Chicken Desserts',  # New category
    'slug': 'chicken-desserts',
    'description': 'Sweet chicken-based desserts'
}
```

### Step 2: Add Products for New Category
```python
{
    'category': 'chicken-desserts',  # Use new category slug
    'name': 'Chicken Kulfi',
    'slug': 'chicken-kulfi',
    'description': 'Unique chicken-flavored dessert',
    'price': Decimal('199.00'),
    'stock': 30,
    'is_featured': False,
    'image': 'https://images.unsplash.com/photo-XXXXXX?w=800&q=80'
}
```

### Step 3: Run Populate Command
```bash
python manage.py populate_data
```

---

## Bulk Import from CSV

### Step 1: Create CSV File
Create `import_products.csv`:

```csv
name,slug,description,price,compare_price,stock,is_featured,category_slug,image
Chicken Pakora Supreme,chicken-pakora-supreme,Extra crispy pakoras,279.00,329.00,50,true,chicken-starters,https://images.unsplash.com/photo-XXXXX?w=800&q=80
```

### Step 2: Create Import Script
Create `products/management/commands/import_products.py`:

```python
import csv
from django.core.management.base import BaseCommand
from products.models import Product, Category
from decimal import Decimal

class Command(BaseCommand):
    help = 'Import products from CSV'

    def handle(self, *args, **kwargs):
        with open('import_products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = Category.objects.get(slug=row['category_slug'])
                Product.objects.get_or_create(
                    slug=row['slug'],
                    defaults={
                        'name': row['name'],
                        'description': row['description'],
                        'price': Decimal(row['price']),
                        'compare_price': Decimal(row['compare_price']) if row['compare_price'] else None,
                        'stock': int(row['stock']),
                        'is_featured': row['is_featured'].lower() == 'true',
                        'category': category,
                        'image': row['image']
                    }
                )
                self.stdout.write(f"Imported: {row['name']}")
```

### Step 3: Run Import
```bash
python manage.py import_products
```

---

## Testing New Products

### 1. Check in Admin Panel
```
http://localhost:8000/admin/products/product/
```

### 2. Check via API
```bash
curl http://localhost:8000/api/products/products | jq '.results[] | {name, image}'
```

### 3. Verify Image Loads
```bash
# Test specific product
curl http://localhost:8000/api/products/chicken-pakora-supreme
```

### 4. View in Frontend
Navigate to your frontend:
- `/products` - All products
- `/products/chicken-pakora-supreme` - Specific product
- `/categories/chicken-starters` - Category page

---

## Troubleshooting

### Image Not Showing?
1. Check image URL is valid (visit in browser)
2. Ensure HTTPS (not HTTP)
3. Check CORS headers if loading from external source
4. Verify URL has no typos

### Product Not Created?
1. Check slug is unique
2. Ensure category exists
3. Verify price is Decimal, not string
4. Check for validation errors in console

### Database Issues?
```bash
# Reset and repopulate
rm db.sqlite3
python manage.py migrate
python manage.py populate_data
```

---

## Quick Reference

### Command Cheat Sheet
```bash
# Create product via shell
python manage.py shell

# Run populate script
python manage.py populate_data

# Access admin panel
python manage.py runserver
# Visit: http://localhost:8000/admin

# Check database
python manage.py dbshell
SELECT COUNT(*) FROM products_product;

# Export products to JSON
python manage.py dumpdata products.Product --indent 2 > products.json
```

---

## Pro Tips

💡 **Reuse Images**: It's okay to use the same image URL for similar products  
💡 **Featured Products**: Set `is_featured=True` for homepage display  
💡 **Stock Management**: Update stock regularly for accurate inventory  
💡 **Pricing**: Use `compare_price` to show discounts  
💡 **SEO**: Use descriptive slugs (e.g., `spicy-chicken-tikka` not `product-123`)  

---

## Need Help?

- Check Django logs: `python manage.py runserver` output
- Use Django shell: `python manage.py shell`
- Test in admin panel first before using API
- Always backup database before bulk changes

Happy product adding! 🎉
