from django.core.management.base import BaseCommand
from products.models import Product, Category


class Command(BaseCommand):
    help = 'Update product images with proper Unsplash images'

    def handle(self, *args, **kwargs):
        # High-quality Unsplash images for each category
        
        # Electronics category images
        electronics_images = {
            'Wireless Headphones': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80',
            'Smartphone': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&q=80',
            'Laptop': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&q=80',
            'Smart Watch': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&q=80',
            'Bluetooth Speaker': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800&q=80',
            '4K Monitor': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&q=80',
            'Gaming Mouse': 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=800&q=80',
            'Mechanical Keyboard': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&q=80',
            'Webcam': 'https://images.unsplash.com/photo-1585509133616-64a2c9e71869?w=800&q=80',
            'USB-C Hub': 'https://images.unsplash.com/photo-1625948515291-69613efd103f?w=800&q=80',
        }
        
        # Clothing category images
        clothing_images = {
            'Classic White T-Shirt': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800&q=80',
            'Denim Jeans': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=800&q=80',
            'Leather Jacket': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=800&q=80',
            'Summer Dress': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=800&q=80',
            'Hoodie': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800&q=80',
            'Formal Shirt': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=800&q=80',
            'Chinos': 'https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=800&q=80',
            'Blazer': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&q=80',
            'Cardigan': 'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=800&q=80',
            'Polo Shirt': 'https://images.unsplash.com/photo-1586363104862-3a5e2ab60d99?w=800&q=80',
        }
        
        # Books category images
        books_images = {
            'The Great Gatsby': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=800&q=80',
            'To Kill a Mockingbird': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800&q=80',
            '1984': 'https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=800&q=80',
            'Harry Potter Series': 'https://images.unsplash.com/photo-1621351183012-e2f9972dd9bf?w=800&q=80',
            'The Hobbit': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=800&q=80',
            'Pride and Prejudice': 'https://images.unsplash.com/photo-1524578271613-d550eacf6090?w=800&q=80',
            'The Catcher in the Rye': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&q=80',
            'Lord of the Flies': 'https://images.unsplash.com/photo-1519682577862-22b62b24e493?w=800&q=80',
            'Animal Farm': 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800&q=80',
            'Brave New World': 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=800&q=80',
        }
        
        # Home & Kitchen category images
        home_kitchen_images = {
            'Coffee Maker': 'https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=800&q=80',
            'Blender': 'https://images.unsplash.com/photo-1585515320310-259814833e62?w=800&q=80',
            'Air Fryer': 'https://images.unsplash.com/photo-1624806992928-e5a6d0e9f07e?w=800&q=80',
            'Toaster': 'https://images.unsplash.com/photo-1604904612715-47bf8d0a9e5c?w=800&q=80',
            'Microwave Oven': 'https://images.unsplash.com/photo-1585659722983-3a675dabf23d?w=800&q=80',
            'Electric Kettle': 'https://images.unsplash.com/photo-1563788835274-77dc83151d86?w=800&q=80',
            'Food Processor': 'https://images.unsplash.com/photo-1601924357840-3e6e6e7e3e06?w=800&q=80',
            'Stand Mixer': 'https://images.unsplash.com/photo-1578643463396-0997cb5328c1?w=800&q=80',
            'Pressure Cooker': 'https://images.unsplash.com/photo-1585515320310-259814833e62?w=800&q=80',
            'Rice Cooker': 'https://images.unsplash.com/photo-1556911220-bff31c812dba?w=800&q=80',
        }
        
        # Sports & Fitness category images
        sports_images = {
            'Yoga Mat': 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=800&q=80',
            'Dumbbells Set': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800&q=80',
            'Resistance Bands': 'https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=800&q=80',
            'Jump Rope': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800&q=80',
            'Foam Roller': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&q=80',
            'Protein Shaker': 'https://images.unsplash.com/photo-1622484211850-7b6e12b9ec5b?w=800&q=80',
            'Gym Bag': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&q=80',
            'Running Shoes': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&q=80',
            'Fitness Tracker': 'https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=800&q=80',
            'Water Bottle': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=800&q=80',
        }
        
        # Diwali Sweets category images
        diwali_sweets_images = {
            'Kaju Katli': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Gulab Jamun': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=800&q=80',
            'Rasgulla': 'https://images.unsplash.com/photo-1606855664257-833d08228a0e?w=800&q=80',
            'Jalebi': 'https://images.unsplash.com/photo-1626176966167-0f0df6082090?w=800&q=80',
            'Barfi': 'https://images.unsplash.com/photo-1606471190009-63d2e24c4f59?w=800&q=80',
            'Ladoo': 'https://images.unsplash.com/photo-1631452180534-f8f5d21e3291?w=800&q=80',
            'Soan Papdi': 'https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=800&q=80',
            'Mysore Pak': 'https://images.unsplash.com/photo-1606855664269-833d08228a0e?w=800&q=80',
            'Peda': 'https://images.unsplash.com/photo-1628863353691-0071c8c1874c?w=800&q=80',
            'Kheer': 'https://images.unsplash.com/photo-1589638302337-e8193fe0e90c?w=800&q=80',
            'Halwa': 'https://images.unsplash.com/photo-1606471190009-63d2e24c4f59?w=800&q=80',
            'Ras Malai': 'https://images.unsplash.com/photo-1606855664257-833d08228a0e?w=800&q=80',
        }
        
        # Combine all image mappings
        all_images = {
            **electronics_images,
            **clothing_images,
            **books_images,
            **home_kitchen_images,
            **sports_images,
            **diwali_sweets_images,
        }
        
        # Update category images
        category_images = {
            'Electronics': 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=800&q=80',
            'Clothing': 'https://images.unsplash.com/photo-1441984904996-e0b6ba687e04?w=800&q=80',
            'Books': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800&q=80',
            'Home & Kitchen': 'https://images.unsplash.com/photo-1556911220-bff31c812dba?w=800&q=80',
            'Sports & Fitness': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800&q=80',
            'Diwali Sweets': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
        }
        
        updated_categories = 0
        for category_name, image_url in category_images.items():
            try:
                category = Category.objects.get(name=category_name)
                category.image = image_url
                category.save()
                updated_categories += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Updated category: {category_name}')
                )
            except Category.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'! Category not found: {category_name}')
                )
        
        # Update product images
        updated_products = 0
        not_found = []
        
        for product_name, image_url in all_images.items():
            try:
                product = Product.objects.get(name=product_name)
                product.image = image_url
                product.save()
                updated_products += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Updated product: {product_name}')
                )
            except Product.DoesNotExist:
                not_found.append(product_name)
        
        # Summary
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Image update complete!'
            )
        )
        self.stdout.write(f'   Categories updated: {updated_categories}')
        self.stdout.write(f'   Products updated: {updated_products}')
        
        if not_found:
            self.stdout.write(
                self.style.WARNING(f'\n⚠ Products not found in database: {len(not_found)}')
            )
            for name in not_found:
                self.stdout.write(f'   - {name}')
