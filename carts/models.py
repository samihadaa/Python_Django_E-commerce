from django.db import models
from store.models import Product

from django.urls import reverse
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class cartItem(models.Model):
    product = models.ForeignKey(Product,models.CASCADE)
    cart = models.ForeignKey(Cart, models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product

    def sub_total(self):
        return self.product.price * self.quantity
     