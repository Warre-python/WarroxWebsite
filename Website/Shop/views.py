from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all()
    return render(request, 'frontend/shop/shop.html', {'products': products})

