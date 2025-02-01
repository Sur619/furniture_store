from atexit import register
from django.contrib import admin

# Register your models here.
from goods.models import categories, products

# admin.site.register(categories)
# admin.site.register(products)

@admin.register(categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
