from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

from goods.models import products

# Create your views here.


def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        goods = products.objects.all()
    else:
        goods = get_list_or_404(products.objects.filter(category__slug=category_slug))

    paginator =  Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {"title": "Home - catalog",
                "goods": current_page,
                "slug_url":category_slug
                }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = products.objects.get(slug = product_slug)
    context = {
        "product": product
    }
    
    return render(request, "goods/product.html", context=context)
