from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, default=False)
    featured = models.BooleanField(blank=True, default=False)

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'my_id': self.id})      # or f"product/{self.id}/"
