from django.core.management.base import BaseCommand
from products.models import Product, Category


class Command(BaseCommand):
    help = 'Fix all product images with proper, relevant Unsplash images'

    def handle(self, *args, **kwargs):
        
        # Category images
        category_images = {
            'Diwali Sweets': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Chicken Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80',
            'Chicken Chinese': 'https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=800&q=80',
            'Chicken Combo Meals': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
            'Chicken Curries': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
            'Chicken Fast Food': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
            'Chicken Rolls & Wraps': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=800&q=80',
            'Chicken Starters': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=800&q=80',
            'Fried Chicken': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
            'Grilled Chicken': 'https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=800&q=80',
            'Tandoori Chicken': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
        }
        
        # Product images - Diwali Sweets
        diwali_sweets = {
            'Kaju Katli': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Kaju Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Pista Barfi': 'https://images.unsplash.com/photo-1606471192009-7b6188493e33?w=800&q=80',
            'Badam Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Plain Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Kesar Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Coconut Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Malai Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Chocolate Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Mango Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Dry Fruit Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Anjeer Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Dodha Barfi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Gulab Jamun': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=800&q=80',
            'Kala Jamun': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=800&q=80',
            'Rasgulla': 'https://images.unsplash.com/photo-1606855664257-833d08228a0e?w=800&q=80',
            'Rasmalai': 'https://images.unsplash.com/photo-1606855664257-833d08228a0e?w=800&q=80',
            'Jalebi': 'https://images.unsplash.com/photo-1626176966167-0f0df6082090?w=800&q=80',
            'Imarti': 'https://images.unsplash.com/photo-1626176966167-0f0df6082090?w=800&q=80',
            'Moti Choor Laddoo': 'https://images.unsplash.com/photo-1631452180534-f8f5d21e3291?w=800&q=80',
            'Besan Laddoo': 'https://images.unsplash.com/photo-1631452180534-f8f5d21e3291?w=800&q=80',
            'Boondi Laddoo': 'https://images.unsplash.com/photo-1631452180534-f8f5d21e3291?w=800&q=80',
            'Gond Laddoo': 'https://images.unsplash.com/photo-1631452180534-f8f5d21e3291?w=800&q=80',
            'Peda': 'https://images.unsplash.com/photo-1628863353691-0071c8c1874c?w=800&q=80',
            'Kesar Peda': 'https://images.unsplash.com/photo-1628863353691-0071c8c1874c?w=800&q=80',
            'Kalakand': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Milk Cake': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Sohan Papdi': 'https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=800&q=80',
            'Patisa': 'https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=800&q=80',
            'Gajar Halwa': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Moong Dal Halwa': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Karachi Halwa': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Soan Halwa': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Petha': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Balushahi': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Kheer Mohan': 'https://images.unsplash.com/photo-1589638302337-e8193fe0e90c?w=800&q=80',
            'Sandesh': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Cham Cham': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
            'Pinni': 'https://images.unsplash.com/photo-1631452180534-f8f5d21e3291?w=800&q=80',
            'Kesar Pista Roll': 'https://images.unsplash.com/photo-1606471191009-63d2e24c4f59?w=800&q=80',
        }
        
        # Chicken Starters
        chicken_starters = {
            'Chicken 65': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=800&q=80',
            'Chicken Tikka': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
            'Chicken Lollipop': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=800&q=80',
            'Chicken Wings': 'https://images.unsplash.com/photo-1608039829572-78524f79c4c7?w=800&q=80',
            'Chicken Seekh Kebab': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
            'Chicken Pakora': 'https://images.unsplash.com/photo-1562967914-608f82629710?w=800&q=80',
        }
        
        # Chicken Curries
        chicken_curries = {
            'Butter Chicken': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=800&q=80',
            'Kadai Chicken': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
            'Chicken Tikka Masala': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
            'Chicken Korma': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
            'Chicken Vindaloo': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
            'Chicken Chettinad': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
            'Chicken Saag': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&q=80',
        }
        
        # Chicken Biryani
        chicken_biryani = {
            'Hyderabadi Chicken Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80',
            'Chicken Dum Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80',
            'Kolkata Chicken Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80',
            'Chicken Tikka Biryani': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80',
            'Chicken Fried Rice': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800&q=80',
            'Chicken Pulao': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=800&q=80',
        }
        
        # Tandoori Chicken
        tandoori_chicken = {
            'Tandoori Chicken Full': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
            'Tandoori Chicken Half': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
            'Chicken Malai Tikka': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
            'Chicken Hariyali Tikka': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
            'Chicken Reshmi Kebab': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=800&q=80',
        }
        
        # Chicken Chinese
        chicken_chinese = {
            'Chicken Chilli': 'https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=800&q=80',
            'Chicken Manchurian': 'https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=800&q=80',
            'Chicken Schezwan': 'https://images.unsplash.com/photo-1617093727343-374698b1b08d?w=800&q=80',
            'Chicken Hakka Noodles': 'https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=800&q=80',
            'Chicken Schezwan Noodles': 'https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=800&q=80',
            'Chicken Szechuan Rice': 'https://images.unsplash.com/photo-1512058564366-18510be2db19?w=800&q=80',
        }
        
        # Chicken Fast Food
        chicken_fast_food = {
            'Chicken Burger': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80',
            'Grilled Chicken Burger': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80',
            'Spicy Chicken Burger': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80',
            'Chicken Nuggets': 'https://images.unsplash.com/photo-1562967916-ca05d44f4c55?w=800&q=80',
            'Chicken Popcorn': 'https://images.unsplash.com/photo-1562967916-ca05d44f4c55?w=800&q=80',
            'Chicken Pizza': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=800&q=80',
        }
        
        # Chicken Rolls & Wraps
        chicken_rolls = {
            'Chicken Kathi Roll': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=800&q=80',
            'Chicken Tikka Roll': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=800&q=80',
            'Chicken Shawarma': 'https://images.unsplash.com/photo-1529006557810-274b9b2fc783?w=800&q=80',
            'Chicken Wrap': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=800&q=80',
            'Chicken Frankie': 'https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=800&q=80',
        }
        
        # Fried Chicken
        fried_chicken = {
            'Crispy Fried Chicken (4 Pieces)': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
            'Crispy Fried Chicken (8 Pieces)': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
            'Spicy Fried Chicken': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
            'Korean Fried Chicken': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=800&q=80',
            'Chicken Strips': 'https://images.unsplash.com/photo-1562967916-ca05d44f4c55?w=800&q=80',
        }
        
        # Grilled Chicken
        grilled_chicken = {
            'Grilled Chicken Breast': 'https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=800&q=80',
            'BBQ Grilled Chicken': 'https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=800&q=80',
            'Peri Peri Grilled Chicken': 'https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=800&q=80',
            'Lemon Herb Grilled Chicken': 'https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=800&q=80',
            'Grilled Chicken Salad': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=800&q=80',
        }
        
        # Chicken Combo Meals
        combo_meals = {
            'Chicken Biryani Combo': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
            'Butter Chicken Combo': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
            'Fried Chicken Combo': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
            'Tandoori Chicken Combo': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
            'Chicken Roll Combo': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
            'Family Chicken Feast': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
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
                f'\n✅ Image update complete!'
            )
        )
        self.stdout.write(f'   Categories updated: {updated_categories}')
        self.stdout.write(f'   Products updated: {updated_products}')
        self.stdout.write(f'   Total products in database: {Product.objects.count()}')
        
        if not_found:
            self.stdout.write(
                self.style.WARNING(f'\n⚠ Products not found: {len(not_found)}')
            )
