from tkinter import CASCADE
from django.db import models

from goods.models import products
from users.models import User

# Create your models here.


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(to=products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cart"


    def products_price(self):
        if self.discount:
            return round(self.sell_price() * self.quantity,2)
        

    def __str__(self):
        return f"Cart of {self.username} | product {self.product} | quantuty {self.quantity}"


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0