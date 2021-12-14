from django.shortcuts import render
from .models import Category, Product


# Create your views here.

# This will allow categories to be accessible to every views, it need to be added to settings.py as well
def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
    })
