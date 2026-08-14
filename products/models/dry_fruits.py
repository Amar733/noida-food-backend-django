from django.db import models


class DryFruit(models.Model):
    """
    Dry fruit item model with auto-generated unique ID.
    
    Fields:
    - id: Auto-generated unique identifier (primary key)
    - name: Item name (unique)
    - price: Item price
    - image: Image URL
    - description: Item description
    - created_at: Auto-generated timestamp
    - updated_at: Auto-updated timestamp
    """
    
    # Auto-generated unique ID (Django creates this implicitly, made explicit here)
    id = models.AutoField(primary_key=True)
    
    # Item fields
    name = models.CharField(max_length=300, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=500)
    description = models.TextField(blank=True, default='')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']  # Order by ID (most natural order)
        indexes = [
            models.Index(fields=['id']),  # Ensure ID is indexed
        ]

    def __str__(self):
        return f"ID: {self.id} - {self.name}"
