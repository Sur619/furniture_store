import select
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import categories

# Create your views here.


def index(request):
    categoriess = categories.objects.all()
    context = {
        "title": "Home - main page",
        "content": "FURNITURE HOME",
        "categoriess": categoriess
    }
    return render(request, 'main/index.html', context)



def about(request):
    context = {
        "title": "home about us",
        "content": "about us"
        "text_on_page"
    }
    return render(request, 'main/about.html', context)