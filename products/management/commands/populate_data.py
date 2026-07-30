from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Category, Product
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database with sample data...')

        # Create categories
        categories_data = [
            {
                'name': 'Electronics',
                'slug': 'electronics',
                'description': 'Electronic devices and accessories'
            },
            {
                'name': 'Clothing',
                'slug': 'clothing',
                'description': 'Fashion and apparel'
            },
            {
                'name': 'Books',
                'slug': 'books',
                'description': 'Books and educational materials'
            },
            {
                'name': 'Home & Kitchen',
                'slug': 'home-kitchen',
                'description': 'Home appliances and kitchen items'
            },
            {
                'name': 'Sports',
                'slug': 'sports',
                'description': 'Sports equipment and fitness gear'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            categories[cat_data['slug']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            {
                'category': 'electronics',
                'name': 'Wireless Headphones',
                'slug': 'wireless-headphones',
                'description': 'High-quality wireless headphones with noise cancellation',
                'price': Decimal('2999.00'),
                'compare_price': Decimal('4999.00'),
                'stock': 50,
                'is_featured': True
            },
            {
                'category': 'electronics',
                'name': 'Smart Watch',
                'slug': 'smart-watch',
                'description': 'Feature-rich smartwatch with fitness tracking',
                'price': Decimal('5999.00'),
                'compare_price': Decimal('8999.00'),
                'stock': 30,
                'is_featured': True
            },
            {
                'category': 'electronics',
                'name': 'Bluetooth Speaker',
                'slug': 'bluetooth-speaker',
                'description': 'Portable Bluetooth speaker with amazing sound quality',
                'price': Decimal('1999.00'),
                'compare_price': Decimal('2999.00'),
                'stock': 100,
                'is_featured': False
            },
            {
                'category': 'clothing',
                'name': 'Mens T-Shirt',
                'slug': 'mens-t-shirt',
                'description': 'Comfortable cotton t-shirt for men',
                'price': Decimal('499.00'),
                'compare_price': Decimal('799.00'),
                'stock': 200,
                'is_featured': False
            },
            {
                'category': 'clothing',
                'name': 'Womens Dress',
                'slug': 'womens-dress',
                'description': 'Elegant dress for women',
                'price': Decimal('1299.00'),
                'compare_price': Decimal('1999.00'),
                'stock': 75,
                'is_featured': True
            },
            {
                'category': 'books',
                'name': 'Python Programming Book',
                'slug': 'python-programming-book',
                'description': 'Comprehensive guide to Python programming',
                'price': Decimal('599.00'),
                'stock': 150,
                'is_featured': False
            },
            {
                'category': 'home-kitchen',
                'name': 'Coffee Maker',
                'slug': 'coffee-maker',
                'description': 'Automatic coffee maker for home use',
                'price': Decimal('3499.00'),
                'compare_price': Decimal('4999.00'),
                'stock': 40,
                'is_featured': True
            },
            {
                'category': 'sports',
                'name': 'Yoga Mat',
                'slug': 'yoga-mat',
                'description': 'Non-slip yoga mat for exercises',
                'price': Decimal('799.00'),
                'compare_price': Decimal('1299.00'),
                'stock': 120,
                'is_featured': False
            }
        ]

        for prod_data in products_data:
            category_slug = prod_data.pop('category')
            prod_data['category'] = categories[category_slug]
            
            product, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults=prod_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))
        self.stdout.write(f'Created {Category.objects.count()} categories')
        self.stdout.write(f'Created {Product.objects.count()} products')
