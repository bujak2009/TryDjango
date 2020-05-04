from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, default=False)
    featured = models.BooleanField(blank=True)

