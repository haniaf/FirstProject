from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(default="this is cool!")
    featured = models.BooleanField(default=False)

    def get_absolute_urls(self):
        return reverse("products: product-detail", kwargs={"id": self.id})