from django.db import models
from apps.categories.models import Category

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=255)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    stock = models.PositiveIntegerField(default=0)

    sku = models.CharField(
        max_length=100,
        unique=True
    )

    image = models.ImageField(
        upload_to="products/",
        null=True,
        blank=True
    )

    fabric = models.CharField(
        max_length=100,
        blank=True
    )

    color = models.CharField(
        max_length=100,
        blank=True
    )

    weight = models.CharField(
        max_length=50,
        blank=True
    )

    is_featured = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name