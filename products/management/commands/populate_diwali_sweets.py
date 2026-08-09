from django.core.management.base import BaseCommand
from products.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populate database with Diwali sweets data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database with Diwali sweets...')

        # Create Diwali Sweets category
        category_data = {
            'name': 'Diwali Sweets',
            'slug': 'diwali-sweets',
            'description': 'Traditional Diwali sweets and mithais from Delhi-NCR',
            'image': 'https://images.pexels.com/photos/3026808/pexels-photo-3026808.jpeg?auto=compress&cs=tinysrgb&w=800',
            'is_active': True
        }

        category, created = Category.objects.get_or_create(
            slug=category_data['slug'],
            defaults=category_data
        )
        if created:
            self.stdout.write(f'Created category: {category.name}')

        # Diwali sweets products with base types
        products_data = [
            {
                'name': 'Kaju Katli',
                'slug': 'kaju-katli',
                'description': 'Premium cashew-based diamond-shaped sweet (Cashew)',
                'price': Decimal('699.00'),
                'compare_price': Decimal('799.00'),
                'stock': 100,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/6787374/pexels-photo-6787374.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Kaju Barfi',
                'slug': 'kaju-barfi',
                'description': 'Rich cashew fudge square (Cashew)',
                'price': Decimal('649.00'),
                'compare_price': Decimal('749.00'),
                'stock': 95,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/6787376/pexels-photo-6787376.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Pista Barfi',
                'slug': 'pista-barfi',
                'description': 'Delicious pistachio barfi (Dry fruit)',
                'price': Decimal('729.00'),
                'compare_price': Decimal('829.00'),
                'stock': 80,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/5561446/pexels-photo-5561446.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Badam Barfi',
                'slug': 'badam-barfi',
                'description': 'Traditional almond barfi (Almond)',
                'price': Decimal('679.00'),
                'stock': 90,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/3026808/pexels-photo-3026808.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Milk Cake',
                'slug': 'milk-cake',
                'description': 'Classic milk-based sweet (Milk/khoya)',
                'price': Decimal('449.00'),
                'compare_price': Decimal('499.00'),
                'stock': 120,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/7362647/pexels-photo-7362647.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Kalakand',
                'slug': 'kalakand',
                'description': 'Soft milk sweet with granular texture (Milk)',
                'price': Decimal('399.00'),
                'stock': 110,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/5560763/pexels-photo-5560763.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Moti Choor Laddoo',
                'slug': 'moti-choor-laddoo',
                'description': 'Pearl-sized boondi laddoo (Besan)',
                'price': Decimal('349.00'),
                'compare_price': Decimal('399.00'),
                'stock': 150,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/6607179/pexels-photo-6607179.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Besan Laddoo',
                'slug': 'besan-laddoo',
                'description': 'Traditional gram flour laddoo (Besan)',
                'price': Decimal('329.00'),
                'stock': 140,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/5560766/pexels-photo-5560766.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Boondi Laddoo',
                'slug': 'boondi-laddoo',
                'description': 'Classic boondi laddoo (Besan)',
                'price': Decimal('319.00'),
                'stock': 145,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6607180/pexels-photo-6607180.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Gond Laddoo',
                'slug': 'gond-laddoo',
                'description': 'Winter special laddoo with edible gum (Ghee/dry fruit)',
                'price': Decimal('549.00'),
                'compare_price': Decimal('629.00'),
                'stock': 70,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/5560764/pexels-photo-5560764.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Pinni',
                'slug': 'pinni',
                'description': 'Punjabi winter sweet (Atta/ghee)',
                'price': Decimal('379.00'),
                'stock': 85,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6608268/pexels-photo-6608268.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Coconut Barfi',
                'slug': 'coconut-barfi',
                'description': 'Sweet coconut barfi (Coconut)',
                'price': Decimal('369.00'),
                'stock': 100,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6787373/pexels-photo-6787373.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Plain Barfi',
                'slug': 'plain-barfi',
                'description': 'Simple khoya barfi (Khoya)',
                'price': Decimal('429.00'),
                'stock': 105,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/3026808/pexels-photo-3026808.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Kesar Barfi',
                'slug': 'kesar-barfi',
                'description': 'Saffron-flavored khoya barfi (Khoya/saffron)',
                'price': Decimal('499.00'),
                'compare_price': Decimal('549.00'),
                'stock': 95,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/5560761/pexels-photo-5560761.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Gulab Jamun',
                'slug': 'gulab-jamun',
                'description': 'Classic rose-flavored milk balls in syrup (Khoya)',
                'price': Decimal('299.00'),
                'stock': 160,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/6607176/pexels-photo-6607176.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Kala Jamun',
                'slug': 'kala-jamun',
                'description': 'Dark brown jamun variety (Khoya)',
                'price': Decimal('319.00'),
                'stock': 130,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6607177/pexels-photo-6607177.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Rasgulla',
                'slug': 'rasgulla',
                'description': 'Soft spongy cottage cheese balls in sugar syrup (Chhena)',
                'price': Decimal('279.00'),
                'stock': 140,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/5560762/pexels-photo-5560762.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Rasmalai',
                'slug': 'rasmalai',
                'description': 'Cottage cheese dumplings in sweet milk (Chhena/milk)',
                'price': Decimal('349.00'),
                'compare_price': Decimal('399.00'),
                'stock': 125,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/7362648/pexels-photo-7362648.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Cham Cham',
                'slug': 'cham-cham',
                'description': 'Bengali sweet with khoya coating (Bengali)',
                'price': Decimal('329.00'),
                'stock': 110,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6787372/pexels-photo-6787372.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Sandesh',
                'slug': 'sandesh',
                'description': 'Bengali cottage cheese sweet (Bengali)',
                'price': Decimal('359.00'),
                'stock': 105,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/3026807/pexels-photo-3026807.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Peda',
                'slug': 'peda',
                'description': 'Traditional round khoya sweet (Khoya)',
                'price': Decimal('379.00'),
                'stock': 120,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6787371/pexels-photo-6787371.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Kesar Peda',
                'slug': 'kesar-peda',
                'description': 'Saffron-flavored peda (Khoya)',
                'price': Decimal('429.00'),
                'stock': 100,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6787370/pexels-photo-6787370.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Sohan Papdi',
                'slug': 'sohan-papdi',
                'description': 'Flaky, crispy sweet (Flour/ghee)',
                'price': Decimal('269.00'),
                'stock': 130,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6608269/pexels-photo-6608269.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Patisa',
                'slug': 'patisa',
                'description': 'Layered flaky sweet (Flour/ghee)',
                'price': Decimal('289.00'),
                'stock': 115,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6608270/pexels-photo-6608270.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Imarti',
                'slug': 'imarti',
                'description': 'Flower-shaped crispy sweet in sugar syrup (Urad dal)',
                'price': Decimal('319.00'),
                'stock': 105,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/7362646/pexels-photo-7362646.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Jalebi',
                'slug': 'jalebi',
                'description': 'Spiral-shaped crispy sweet in sugar syrup (Flour)',
                'price': Decimal('249.00'),
                'stock': 150,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/6607178/pexels-photo-6607178.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Balushahi',
                'slug': 'balushahi',
                'description': 'Soft, flaky donut-like sweet (Flour/ghee)',
                'price': Decimal('299.00'),
                'stock': 120,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6608267/pexels-photo-6608267.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Kheer Mohan',
                'slug': 'kheer-mohan',
                'description': 'Cottage cheese sweet in thick milk (Chhena)',
                'price': Decimal('339.00'),
                'stock': 95,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/5560765/pexels-photo-5560765.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Karachi Halwa',
                'slug': 'karachi-halwa',
                'description': 'Translucent, chewy cornflour sweet (Cornflour)',
                'price': Decimal('449.00'),
                'stock': 85,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/5560768/pexels-photo-5560768.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Gajar Halwa',
                'slug': 'gajar-halwa',
                'description': 'Carrot pudding with milk and ghee (Carrot/milk)',
                'price': Decimal('329.00'),
                'compare_price': Decimal('379.00'),
                'stock': 100,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/7362645/pexels-photo-7362645.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Moong Dal Halwa',
                'slug': 'moong-dal-halwa',
                'description': 'Rich lentil halwa with ghee (Dal/ghee)',
                'price': Decimal('399.00'),
                'stock': 90,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/5560767/pexels-photo-5560767.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Petha',
                'slug': 'petha',
                'description': 'Translucent ash gourd sweet from Agra (Ash gourd)',
                'price': Decimal('279.00'),
                'stock': 110,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6608271/pexels-photo-6608271.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Soan Halwa',
                'slug': 'soan-halwa',
                'description': 'Flaky, fibrous texture halwa (Flour/ghee)',
                'price': Decimal('349.00'),
                'stock': 95,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6608272/pexels-photo-6608272.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Dodha Barfi',
                'slug': 'dodha-barfi',
                'description': 'Thick milk and grain barfi (Grain/milk)',
                'price': Decimal('429.00'),
                'stock': 85,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6787375/pexels-photo-6787375.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Anjeer Barfi',
                'slug': 'anjeer-barfi',
                'description': 'Fig and dry fruit barfi (Fig/dry fruit)',
                'price': Decimal('579.00'),
                'compare_price': Decimal('649.00'),
                'stock': 75,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/5561447/pexels-photo-5561447.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Dry Fruit Barfi',
                'slug': 'dry-fruit-barfi',
                'description': 'Mixed nuts barfi (Mixed nuts)',
                'price': Decimal('629.00'),
                'compare_price': Decimal('699.00'),
                'stock': 80,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/6787369/pexels-photo-6787369.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Kesar Pista Roll',
                'slug': 'kesar-pista-roll',
                'description': 'Premium saffron pistachio roll (Dry fruit)',
                'price': Decimal('749.00'),
                'compare_price': Decimal('849.00'),
                'stock': 65,
                'is_featured': True,
                'image': 'https://images.pexels.com/photos/5561448/pexels-photo-5561448.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Mango Barfi',
                'slug': 'mango-barfi',
                'description': 'Seasonal mango-flavored barfi (Milk/mango)',
                'price': Decimal('479.00'),
                'stock': 70,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/5560769/pexels-photo-5560769.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Chocolate Barfi',
                'slug': 'chocolate-barfi',
                'description': 'Modern fusion chocolate mithai (Modern mithai)',
                'price': Decimal('449.00'),
                'stock': 90,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6787368/pexels-photo-6787368.jpeg?auto=compress&cs=tinysrgb&w=800'
            },
            {
                'name': 'Malai Barfi',
                'slug': 'malai-barfi',
                'description': 'Creamy milk barfi (Milk/khoya)',
                'price': Decimal('469.00'),
                'stock': 95,
                'is_featured': False,
                'image': 'https://images.pexels.com/photos/6787367/pexels-photo-6787367.jpeg?auto=compress&cs=tinysrgb&w=800'
            }
        ]

        # Create all products
        for prod_data in products_data:
            prod_data['category'] = category
            
            product, created = Product.objects.get_or_create(
                slug=prod_data['slug'],
                defaults=prod_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        self.stdout.write(self.style.SUCCESS('Successfully populated Diwali sweets!'))
        self.stdout.write(f'Total Diwali sweets products: {Product.objects.filter(category=category).count()}')
