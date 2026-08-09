from django.core.management.base import BaseCommand
from products.models import Product, Category


class Command(BaseCommand):
    help = 'Fix all product images with working Pexels images'

    def handle(self, *args, **kwargs):
        
        # Category images from Pexels
        category_images = {
            'Diwali Sweets': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Biryani': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Chinese': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Combo Meals': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Curries': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Fast Food': 'https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Rolls & Wraps': 'https://images.pexels.com/photos/7595072/pexels-photo-7595072.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Starters': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Fried Chicken': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Grilled Chicken': 'https://images.pexels.com/photos/1127843/pexels-photo-1127843.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Tandoori Chicken': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Product images - Diwali Sweets from Pexels
        diwali_sweets = {
            'Kaju Katli': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kaju Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Pista Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Badam Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Plain Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kesar Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Coconut Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Malai Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chocolate Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Mango Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Dry Fruit Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Anjeer Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Dodha Barfi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Gulab Jamun': 'https://images.pexels.com/photos/3850477/pexels-photo-3850477.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kala Jamun': 'https://images.pexels.com/photos/3850477/pexels-photo-3850477.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Rasgulla': 'https://images.pexels.com/photos/5560763/pexels-photo-5560763.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Rasmalai': 'https://images.pexels.com/photos/5560763/pexels-photo-5560763.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Jalebi': 'https://images.pexels.com/photos/8029707/pexels-photo-8029707.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Imarti': 'https://images.pexels.com/photos/8029707/pexels-photo-8029707.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Moti Choor Laddoo': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Besan Laddoo': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Boondi Laddoo': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Gond Laddoo': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Peda': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kesar Peda': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kalakand': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Milk Cake': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Sohan Papdi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Patisa': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Gajar Halwa': 'https://images.pexels.com/photos/6210930/pexels-photo-6210930.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Moong Dal Halwa': 'https://images.pexels.com/photos/6210930/pexels-photo-6210930.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Karachi Halwa': 'https://images.pexels.com/photos/6210930/pexels-photo-6210930.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Soan Halwa': 'https://images.pexels.com/photos/6210930/pexels-photo-6210930.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Petha': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Balushahi': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kheer Mohan': 'https://images.pexels.com/photos/5560763/pexels-photo-5560763.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Sandesh': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Cham Cham': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Pinni': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kesar Pista Roll': 'https://images.pexels.com/photos/7267767/pexels-photo-7267767.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Chicken Starters from Pexels
        chicken_starters = {
            'Chicken 65': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Tikka': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Lollipop': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Wings': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Seekh Kebab': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Pakora': 'https://images.pexels.com/photos/6210748/pexels-photo-6210748.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Chicken Curries from Pexels
        chicken_curries = {
            'Butter Chicken': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kadai Chicken': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Tikka Masala': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Korma': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Vindaloo': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Chettinad': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Saag': 'https://images.pexels.com/photos/2474661/pexels-photo-2474661.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Chicken Biryani from Pexels
        chicken_biryani = {
            'Hyderabadi Chicken Biryani': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Dum Biryani': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Kolkata Chicken Biryani': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Tikka Biryani': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Fried Rice': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Pulao': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Tandoori Chicken from Pexels
        tandoori_chicken = {
            'Tandoori Chicken Full': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Tandoori Chicken Half': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Malai Tikka': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Hariyali Tikka': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Reshmi Kebab': 'https://images.pexels.com/photos/5410400/pexels-photo-5410400.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Chicken Chinese from Pexels
        chicken_chinese = {
            'Chicken Chilli': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Manchurian': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Schezwan': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Hakka Noodles': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Schezwan Noodles': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Szechuan Rice': 'https://images.pexels.com/photos/2456435/pexels-photo-2456435.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Chicken Fast Food from Pexels
        chicken_fast_food = {
            'Chicken Burger': 'https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Grilled Chicken Burger': 'https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Spicy Chicken Burger': 'https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Nuggets': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Popcorn': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Pizza': 'https://images.pexels.com/photos/2147491/pexels-photo-2147491.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Chicken Rolls & Wraps from Pexels
        chicken_rolls = {
            'Chicken Kathi Roll': 'https://images.pexels.com/photos/7595072/pexels-photo-7595072.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Tikka Roll': 'https://images.pexels.com/photos/7595072/pexels-photo-7595072.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Shawarma': 'https://images.pexels.com/photos/7595072/pexels-photo-7595072.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Wrap': 'https://images.pexels.com/photos/7595072/pexels-photo-7595072.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Frankie': 'https://images.pexels.com/photos/7595072/pexels-photo-7595072.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Fried Chicken from Pexels
        fried_chicken = {
            'Crispy Fried Chicken (4 Pieces)': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Crispy Fried Chicken (8 Pieces)': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Spicy Fried Chicken': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Korean Fried Chicken': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Strips': 'https://images.pexels.com/photos/2280547/pexels-photo-2280547.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Grilled Chicken from Pexels
        grilled_chicken = {
            'Grilled Chicken Breast': 'https://images.pexels.com/photos/1127843/pexels-photo-1127843.jpeg?auto=compress&cs=tinysrgb&w=800',
            'BBQ Grilled Chicken': 'https://images.pexels.com/photos/1127843/pexels-photo-1127843.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Peri Peri Grilled Chicken': 'https://images.pexels.com/photos/1127843/pexels-photo-1127843.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Lemon Herb Grilled Chicken': 'https://images.pexels.com/photos/1127843/pexels-photo-1127843.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Grilled Chicken Salad': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Chicken Combo Meals from Pexels
        combo_meals = {
            'Chicken Biryani Combo': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Butter Chicken Combo': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Fried Chicken Combo': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Tandoori Chicken Combo': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Chicken Roll Combo': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
            'Family Chicken Feast': 'https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=800',
        }
        
        # Combine all images
        all_product_images = {
            **diwali_sweets,
            **chicken_starters,
            **chicken_curries,
            **chicken_biryani,
            **tandoori_chicken,
            **chicken_chinese,
            **chicken_fast_food,
            **chicken_rolls,
            **fried_chicken,
            **grilled_chicken,
            **combo_meals,
        }
        
        # Update categories
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
        
        # Update products
        updated_products = 0
        not_found = []
        
        for product_name, image_url in all_product_images.items():
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
                f'\n✅ Image update complete with Pexels URLs!'
            )
        )
        self.stdout.write(f'   Categories updated: {updated_categories}')
        self.stdout.write(f'   Products updated: {updated_products}')
        self.stdout.write(f'   Total products in database: {Product.objects.count()}')
        
        if not_found:
            self.stdout.write(
                self.style.WARNING(f'\n⚠ Products not found: {len(not_found)}')
            )
