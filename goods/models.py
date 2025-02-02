from email.mime import image
from django.db import models

# Create your models here.


class categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)

    class Meta:
        db_table = "category"


    def __str__(self):
        return  self.name

class products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0.00)
    category = models.ForeignKey(to=categories, on_delete=models.CASCADE)


    class Meta:
        db_table = "product"


    def __str__(self):
        return  self.name    


    def display_id(self):
        return f"{self.id:05}"
    

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100,2)
        
        return self.price