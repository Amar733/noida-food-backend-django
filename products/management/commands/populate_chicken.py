"""
Management command to populate chicken items in the database
"""
from django.core.management.base import BaseCommand
from products.models.chicken import ChickenItem


class Command(BaseCommand):
    help = 'Populate database with sample chicken items'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating chicken items...')
        
        chicken_items = [
            {
                'name': 'Chicken Breast (500g)',
                'price': 249.00,
                'image': 'https://images.pexels.com/photos/2338407/pexels-photo-2338407.jpeg'
            },
            {
                'name': 'Chicken Thighs (500g)',
                'price': 199.00,
                'image': 'https://images.pexels.com/photos/2338407/pexels-photo-2338407.jpeg'
            },
            {
                'name': 'Chicken Wings (500g)',
                'price': 179.00,
                'image': 'https://images.pexels.com/photos/60616/fried-chicken-chicken-fried-crunchy-60616.jpeg'
            },
            {
                'name': 'Whole Chicken (1kg)',
                'price': 399.00,
                'image': 'https://images.pexels.com/photos/2338407/pexels-photo-2338407.jpeg'
            },
            {
                'name': 'Chicken Drumsticks (500g)',
                'price': 189.00,
                'image': 'https://images.pexels.com/photos/60616/fried-chicken-chicken-fried-crunchy-60616.jpeg'
            },
            {
                'name': 'Chicken Mince (500g)',
                'price': 229.00,
                'image': 'https://images.pexels.com/photos/2338407/pexels-photo-2338407.jpeg'
            },
            {
                'name': 'Chicken Liver (250g)',
                'price': 89.00,
                'image': 'https://images.pexels.com/photos/2338407/pexels-photo-2338407.jpeg'
            },
            {
                'name': 'Chicken Nuggets (300g)',
                'price': 159.00,
                'image': 'https://images.pexels.com/photos/60616/fried-chicken-chicken-fried-crunchy-60616.jpeg'
            },
            {
                'name': 'Chicken Sausages (250g)',
                'price': 149.00,
                'image': 'https://images.pexels.com/photos/3688/food-dinner-lunch-unhealthy.jpg'
            },
            {
                'name': 'Marinated Chicken Tikka (500g)',
                'price': 299.00,
                'image': 'https://images.pexels.com/photos/2338407/pexels-photo-2338407.jpeg'
            }
        ]
        
        created_count = 0
        updated_count = 0
        
        for item_data in chicken_items:
            item, created = ChickenItem.objects.update_or_create(
                name=item_data['name'],
                defaults={
                    'price': item_data['price'],
                    'image': item_data['image']
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {item.name}'))
            else:
                updated_count += 1
                self.stdout.write(self.style.WARNING(f'↻ Updated: {item.name}'))
        
        self.stdout.write(self.style.SUCCESS(
            f'\n✓ Successfully populated {created_count} new items and updated {updated_count} existing items'
        ))
