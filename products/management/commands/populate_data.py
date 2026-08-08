from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Category, Product
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database with sample data...')

        # Create categories - Chicken Food Categories
        categories_data = [
            {
                'name': 'Chicken Starters',
                'slug': 'chicken-starters',
                'description': 'Delicious chicken appetizers and starters'
            },
            {
                'name': 'Chicken Curries',
                'slug': 'chicken-curries',
                'description': 'Rich and flavorful chicken curry dishes'
            },
            {
                'name': 'Chicken Biryani',
                'slug': 'chicken-biryani',
                'description': 'Aromatic chicken biryanis and rice dishes'
            },
            {
                'name': 'Tandoori Chicken',
                'slug': 'tandoori-chicken',
                'description': 'Grilled and tandoor-cooked chicken specialties'
            },
            {
                'name': 'Chicken Chinese',
                'slug': 'chicken-chinese',
                'description': 'Indo-Chinese chicken preparations'
            },
            {
                'name': 'Chicken Fast Food',
                'slug': 'chicken-fast-food',
                'description': 'Burgers, wraps, and quick chicken bites'
            },
            {
                'name': 'Chicken Rolls & Wraps',
                'slug': 'chicken-rolls-wraps',
                'description': 'Rolled and wrapped chicken delicacies'
            },
            {
                'name': 'Fried Chicken',
                'slug': 'fried-chicken',
                'description': 'Crispy fried chicken varieties'
            },
            {
                'name': 'Chicken Combo Meals',
                'slug': 'chicken-combo-meals',
                'description': 'Complete chicken meal combos'
            },
            {
                'name': 'Grilled Chicken',
                'slug': 'grilled-chicken',
                'description': 'Healthy grilled chicken options'
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

        # Create products - Chicken Food Items
        products_data = [
            # Chicken Starters
            {
                'category': 'chicken-starters',
                'name': 'Chicken 65',
                'slug': 'chicken-65',
                'description': 'Spicy, deep-fried chicken appetizer with South Indian flavors',
                'price': Decimal('299.00'),
                'compare_price': Decimal('349.00'),
                'stock': 50,
                'is_featured': True
            },
            {
                'category': 'chicken-starters',
                'name': 'Chicken Tikka',
                'slug': 'chicken-tikka',
                'description': 'Marinated chicken cubes grilled to perfection with Indian spices',
                'price': Decimal('279.00'),
                'compare_price': Decimal('329.00'),
                'stock': 45,
                'is_featured': True
            },
            {
                'category': 'chicken-starters',
                'name': 'Chicken Lollipop',
                'slug': 'chicken-lollipop',
                'description': 'Crispy fried chicken wings shaped like lollipops (6 pieces)',
                'price': Decimal('329.00'),
                'compare_price': Decimal('379.00'),
                'stock': 40,
                'is_featured': True
            },
            {
                'category': 'chicken-starters',
                'name': 'Chicken Wings',
                'slug': 'chicken-wings',
                'description': 'Spicy buffalo chicken wings with tangy sauce (8 pieces)',
                'price': Decimal('349.00'),
                'stock': 38,
                'is_featured': False
            },
            {
                'category': 'chicken-starters',
                'name': 'Chicken Seekh Kebab',
                'slug': 'chicken-seekh-kebab',
                'description': 'Minced chicken kebabs with aromatic spices (4 pieces)',
                'price': Decimal('289.00'),
                'stock': 42,
                'is_featured': False
            },
            {
                'category': 'chicken-starters',
                'name': 'Chicken Pakora',
                'slug': 'chicken-pakora',
                'description': 'Chicken fritters in spiced gram flour batter',
                'price': Decimal('249.00'),
                'stock': 50,
                'is_featured': False
            },
            
            # Chicken Curries
            {
                'category': 'chicken-curries',
                'name': 'Butter Chicken',
                'slug': 'butter-chicken',
                'description': 'Tender chicken in rich, creamy tomato-based gravy',
                'price': Decimal('349.00'),
                'compare_price': Decimal('399.00'),
                'stock': 60,
                'is_featured': True
            },
            {
                'category': 'chicken-curries',
                'name': 'Kadai Chicken',
                'slug': 'kadai-chicken',
                'description': 'Spicy chicken curry cooked in traditional kadai with bell peppers',
                'price': Decimal('339.00'),
                'compare_price': Decimal('389.00'),
                'stock': 55,
                'is_featured': True
            },
            {
                'category': 'chicken-curries',
                'name': 'Chicken Tikka Masala',
                'slug': 'chicken-tikka-masala',
                'description': 'Grilled chicken tikka in creamy tomato masala gravy',
                'price': Decimal('359.00'),
                'stock': 50,
                'is_featured': True
            },
            {
                'category': 'chicken-curries',
                'name': 'Chicken Korma',
                'slug': 'chicken-korma',
                'description': 'Mild, creamy chicken curry with cashew and yogurt',
                'price': Decimal('329.00'),
                'stock': 48,
                'is_featured': False
            },
            {
                'category': 'chicken-curries',
                'name': 'Chicken Vindaloo',
                'slug': 'chicken-vindaloo',
                'description': 'Spicy Goan-style chicken curry with vinegar and red chilies',
                'price': Decimal('339.00'),
                'stock': 45,
                'is_featured': False
            },
            {
                'category': 'chicken-curries',
                'name': 'Chicken Chettinad',
                'slug': 'chicken-chettinad',
                'description': 'South Indian spicy chicken curry with roasted spices',
                'price': Decimal('349.00'),
                'stock': 42,
                'is_featured': False
            },
            {
                'category': 'chicken-curries',
                'name': 'Chicken Saag',
                'slug': 'chicken-saag',
                'description': 'Chicken cooked in spinach gravy with aromatic spices',
                'price': Decimal('319.00'),
                'stock': 40,
                'is_featured': False
            },
            
            # Chicken Biryani
            {
                'category': 'chicken-biryani',
                'name': 'Hyderabadi Chicken Biryani',
                'slug': 'hyderabadi-chicken-biryani',
                'description': 'Authentic Hyderabadi-style aromatic chicken biryani',
                'price': Decimal('349.00'),
                'compare_price': Decimal('399.00'),
                'stock': 70,
                'is_featured': True
            },
            {
                'category': 'chicken-biryani',
                'name': 'Chicken Dum Biryani',
                'slug': 'chicken-dum-biryani',
                'description': 'Slow-cooked chicken biryani in sealed pot with saffron',
                'price': Decimal('369.00'),
                'compare_price': Decimal('419.00'),
                'stock': 65,
                'is_featured': True
            },
            {
                'category': 'chicken-biryani',
                'name': 'Kolkata Chicken Biryani',
                'slug': 'kolkata-chicken-biryani',
                'description': 'Bengali-style chicken biryani with potato and egg',
                'price': Decimal('339.00'),
                'stock': 60,
                'is_featured': False
            },
            {
                'category': 'chicken-biryani',
                'name': 'Chicken Tikka Biryani',
                'slug': 'chicken-tikka-biryani',
                'description': 'Biryani made with grilled chicken tikka pieces',
                'price': Decimal('379.00'),
                'stock': 55,
                'is_featured': False
            },
            {
                'category': 'chicken-biryani',
                'name': 'Chicken Fried Rice',
                'slug': 'chicken-fried-rice',
                'description': 'Chinese-style fried rice with chicken and vegetables',
                'price': Decimal('249.00'),
                'stock': 80,
                'is_featured': False
            },
            {
                'category': 'chicken-biryani',
                'name': 'Chicken Pulao',
                'slug': 'chicken-pulao',
                'description': 'Fragrant rice cooked with chicken and whole spices',
                'price': Decimal('279.00'),
                'stock': 70,
                'is_featured': False
            },
            
            # Tandoori Chicken
            {
                'category': 'tandoori-chicken',
                'name': 'Tandoori Chicken Full',
                'slug': 'tandoori-chicken-full',
                'description': 'Whole chicken marinated in yogurt and spices, grilled in tandoor',
                'price': Decimal('599.00'),
                'compare_price': Decimal('699.00'),
                'stock': 30,
                'is_featured': True
            },
            {
                'category': 'tandoori-chicken',
                'name': 'Tandoori Chicken Half',
                'slug': 'tandoori-chicken-half',
                'description': 'Half chicken marinated and grilled to perfection',
                'price': Decimal('329.00'),
                'compare_price': Decimal('379.00'),
                'stock': 45,
                'is_featured': True
            },
            {
                'category': 'tandoori-chicken',
                'name': 'Chicken Malai Tikka',
                'slug': 'chicken-malai-tikka',
                'description': 'Creamy, mildly spiced chicken tikka with cheese',
                'price': Decimal('319.00'),
                'stock': 40,
                'is_featured': False
            },
            {
                'category': 'tandoori-chicken',
                'name': 'Chicken Hariyali Tikka',
                'slug': 'chicken-hariyali-tikka',
                'description': 'Green chicken tikka marinated with mint and coriander',
                'price': Decimal('309.00'),
                'stock': 38,
                'is_featured': False
            },
            {
                'category': 'tandoori-chicken',
                'name': 'Chicken Reshmi Kebab',
                'slug': 'chicken-reshmi-kebab',
                'description': 'Soft and silky chicken kebab with mild spices (6 pieces)',
                'price': Decimal('329.00'),
                'stock': 35,
                'is_featured': False
            },
            
            # Chicken Chinese
            {
                'category': 'chicken-chinese',
                'name': 'Chicken Chilli',
                'slug': 'chicken-chilli',
                'description': 'Spicy Indo-Chinese chicken with bell peppers and onions',
                'price': Decimal('299.00'),
                'compare_price': Decimal('349.00'),
                'stock': 55,
                'is_featured': True
            },
            {
                'category': 'chicken-chinese',
                'name': 'Chicken Manchurian',
                'slug': 'chicken-manchurian',
                'description': 'Deep-fried chicken in spicy Manchurian sauce',
                'price': Decimal('289.00'),
                'stock': 50,
                'is_featured': True
            },
            {
                'category': 'chicken-chinese',
                'name': 'Chicken Schezwan',
                'slug': 'chicken-schezwan',
                'description': 'Spicy Schezwan sauce-based chicken stir-fry',
                'price': Decimal('309.00'),
                'stock': 48,
                'is_featured': False
            },
            {
                'category': 'chicken-chinese',
                'name': 'Chicken Hakka Noodles',
                'slug': 'chicken-hakka-noodles',
                'description': 'Stir-fried noodles with chicken and vegetables',
                'price': Decimal('249.00'),
                'stock': 65,
                'is_featured': False
            },
            {
                'category': 'chicken-chinese',
                'name': 'Chicken Schezwan Noodles',
                'slug': 'chicken-schezwan-noodles',
                'description': 'Spicy Schezwan noodles with chicken',
                'price': Decimal('269.00'),
                'stock': 60,
                'is_featured': False
            },
            {
                'category': 'chicken-chinese',
                'name': 'Chicken Szechuan Rice',
                'slug': 'chicken-szechuan-rice',
                'description': 'Hot and spicy Szechuan-style chicken fried rice',
                'price': Decimal('259.00'),
                'stock': 58,
                'is_featured': False
            },
            
            # Chicken Fast Food
            {
                'category': 'chicken-fast-food',
                'name': 'Chicken Burger',
                'slug': 'chicken-burger',
                'description': 'Crispy chicken patty with lettuce, tomato, and special sauce',
                'price': Decimal('149.00'),
                'compare_price': Decimal('179.00'),
                'stock': 80,
                'is_featured': True
            },
            {
                'category': 'chicken-fast-food',
                'name': 'Grilled Chicken Burger',
                'slug': 'grilled-chicken-burger',
                'description': 'Healthy grilled chicken burger with veggies',
                'price': Decimal('169.00'),
                'compare_price': Decimal('199.00'),
                'stock': 75,
                'is_featured': True
            },
            {
                'category': 'chicken-fast-food',
                'name': 'Spicy Chicken Burger',
                'slug': 'spicy-chicken-burger',
                'description': 'Extra spicy chicken burger with jalapeños',
                'price': Decimal('159.00'),
                'stock': 70,
                'is_featured': False
            },
            {
                'category': 'chicken-fast-food',
                'name': 'Chicken Nuggets',
                'slug': 'chicken-nuggets',
                'description': 'Crispy chicken nuggets with dipping sauce (10 pieces)',
                'price': Decimal('199.00'),
                'stock': 90,
                'is_featured': False
            },
            {
                'category': 'chicken-fast-food',
                'name': 'Chicken Popcorn',
                'slug': 'chicken-popcorn',
                'description': 'Bite-sized crispy chicken pieces (200g)',
                'price': Decimal('179.00'),
                'stock': 85,
                'is_featured': False
            },
            {
                'category': 'chicken-fast-food',
                'name': 'Chicken Pizza',
                'slug': 'chicken-pizza',
                'description': 'Pizza topped with grilled chicken and vegetables',
                'price': Decimal('399.00'),
                'compare_price': Decimal('449.00'),
                'stock': 50,
                'is_featured': True
            },
            
            # Chicken Rolls & Wraps
            {
                'category': 'chicken-rolls-wraps',
                'name': 'Chicken Kathi Roll',
                'slug': 'chicken-kathi-roll',
                'description': 'Kolkata-style chicken roll wrapped in paratha',
                'price': Decimal('149.00'),
                'stock': 70,
                'is_featured': True
            },
            {
                'category': 'chicken-rolls-wraps',
                'name': 'Chicken Tikka Roll',
                'slug': 'chicken-tikka-roll',
                'description': 'Grilled chicken tikka wrapped with onions and chutney',
                'price': Decimal('169.00'),
                'compare_price': Decimal('199.00'),
                'stock': 65,
                'is_featured': True
            },
            {
                'category': 'chicken-rolls-wraps',
                'name': 'Chicken Shawarma',
                'slug': 'chicken-shawarma',
                'description': 'Middle-Eastern style chicken wrap with garlic sauce',
                'price': Decimal('179.00'),
                'stock': 60,
                'is_featured': False
            },
            {
                'category': 'chicken-rolls-wraps',
                'name': 'Chicken Wrap',
                'slug': 'chicken-wrap',
                'description': 'Grilled chicken wrapped in tortilla with fresh veggies',
                'price': Decimal('159.00'),
                'stock': 68,
                'is_featured': False
            },
            {
                'category': 'chicken-rolls-wraps',
                'name': 'Chicken Frankie',
                'slug': 'chicken-frankie',
                'description': 'Mumbai-style chicken frankie with special masala',
                'price': Decimal('139.00'),
                'stock': 75,
                'is_featured': False
            },
            
            # Fried Chicken
            {
                'category': 'fried-chicken',
                'name': 'Crispy Fried Chicken (4 Pieces)',
                'slug': 'crispy-fried-chicken-4pc',
                'description': 'Southern-style crispy fried chicken pieces',
                'price': Decimal('299.00'),
                'compare_price': Decimal('349.00'),
                'stock': 55,
                'is_featured': True
            },
            {
                'category': 'fried-chicken',
                'name': 'Crispy Fried Chicken (8 Pieces)',
                'slug': 'crispy-fried-chicken-8pc',
                'description': 'Family pack - 8 pieces of crispy fried chicken',
                'price': Decimal('549.00'),
                'compare_price': Decimal('649.00'),
                'stock': 40,
                'is_featured': True
            },
            {
                'category': 'fried-chicken',
                'name': 'Spicy Fried Chicken',
                'slug': 'spicy-fried-chicken',
                'description': 'Extra hot and spicy fried chicken (4 pieces)',
                'price': Decimal('319.00'),
                'stock': 48,
                'is_featured': False
            },
            {
                'category': 'fried-chicken',
                'name': 'Korean Fried Chicken',
                'slug': 'korean-fried-chicken',
                'description': 'Korean-style double fried chicken with sweet-spicy glaze',
                'price': Decimal('379.00'),
                'compare_price': Decimal('429.00'),
                'stock': 45,
                'is_featured': True
            },
            {
                'category': 'fried-chicken',
                'name': 'Chicken Strips',
                'slug': 'chicken-strips',
                'description': 'Crispy breaded chicken strips (6 pieces)',
                'price': Decimal('249.00'),
                'stock': 60,
                'is_featured': False
            },
            
            # Grilled Chicken
            {
                'category': 'grilled-chicken',
                'name': 'Grilled Chicken Breast',
                'slug': 'grilled-chicken-breast',
                'description': 'Healthy grilled chicken breast with herbs',
                'price': Decimal('289.00'),
                'stock': 50,
                'is_featured': True
            },
            {
                'category': 'grilled-chicken',
                'name': 'BBQ Grilled Chicken',
                'slug': 'bbq-grilled-chicken',
                'description': 'Grilled chicken with smoky BBQ sauce',
                'price': Decimal('329.00'),
                'compare_price': Decimal('379.00'),
                'stock': 45,
                'is_featured': True
            },
            {
                'category': 'grilled-chicken',
                'name': 'Peri Peri Grilled Chicken',
                'slug': 'peri-peri-grilled-chicken',
                'description': 'Grilled chicken with spicy peri peri seasoning',
                'price': Decimal('339.00'),
                'stock': 42,
                'is_featured': False
            },
            {
                'category': 'grilled-chicken',
                'name': 'Lemon Herb Grilled Chicken',
                'slug': 'lemon-herb-grilled-chicken',
                'description': 'Grilled chicken marinated with lemon and herbs',
                'price': Decimal('299.00'),
                'stock': 48,
                'is_featured': False
            },
            {
                'category': 'grilled-chicken',
                'name': 'Grilled Chicken Salad',
                'slug': 'grilled-chicken-salad',
                'description': 'Fresh salad with grilled chicken and vinaigrette',
                'price': Decimal('269.00'),
                'stock': 55,
                'is_featured': False
            },
            
            # Chicken Combo Meals
            {
                'category': 'chicken-combo-meals',
                'name': 'Chicken Biryani Combo',
                'slug': 'chicken-biryani-combo',
                'description': 'Chicken biryani with raita, salan, and gulab jamun',
                'price': Decimal('399.00'),
                'compare_price': Decimal('499.00'),
                'stock': 50,
                'is_featured': True
            },
            {
                'category': 'chicken-combo-meals',
                'name': 'Butter Chicken Combo',
                'slug': 'butter-chicken-combo',
                'description': 'Butter chicken with 3 naan, rice, and salad',
                'price': Decimal('449.00'),
                'compare_price': Decimal('549.00'),
                'stock': 45,
                'is_featured': True
            },
            {
                'category': 'chicken-combo-meals',
                'name': 'Fried Chicken Combo',
                'slug': 'fried-chicken-combo',
                'description': '4pc fried chicken, fries, coleslaw, and soft drink',
                'price': Decimal('399.00'),
                'stock': 48,
                'is_featured': False
            },
            {
                'category': 'chicken-combo-meals',
                'name': 'Tandoori Chicken Combo',
                'slug': 'tandoori-chicken-combo',
                'description': 'Half tandoori chicken with naan, dal, and raita',
                'price': Decimal('429.00'),
                'stock': 42,
                'is_featured': False
            },
            {
                'category': 'chicken-combo-meals',
                'name': 'Chicken Roll Combo',
                'slug': 'chicken-roll-combo',
                'description': '2 chicken rolls, fries, and beverage',
                'price': Decimal('299.00'),
                'compare_price': Decimal('349.00'),
                'stock': 55,
                'is_featured': False
            },
            {
                'category': 'chicken-combo-meals',
                'name': 'Family Chicken Feast',
                'slug': 'family-chicken-feast',
                'description': '8pc fried chicken, 2 biryanis, naan, and 4 drinks',
                'price': Decimal('999.00'),
                'compare_price': Decimal('1199.00'),
                'stock': 25,
                'is_featured': True
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
