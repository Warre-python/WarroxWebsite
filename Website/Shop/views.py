from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all()
    return render(request, 'frontend/shop/shop.html', {'products': products})

def product(request, slug):
    # Zoek het product op basis van de slug, anders 404 error
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'frontend/shop/product.html', {'product': product})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        request.session['cart'] = cart
        return redirect('product', slug=product.slug)
    return redirect('shop')