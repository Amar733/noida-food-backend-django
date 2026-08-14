from django.db import models


class Product(models.Model):
    """Base product model for the e-commerce system"""
    name = models.CharField(max_length=300, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=500)
    category = models.CharField(max_length=100, default='general')
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Import category-specific models
from .chicken import ChickenItem
from .dry_fruits import DryFruit
from .sweets import Sweet

__all__ = ['Product', 'ChickenItem', 'DryFruit', 'Sweet']
