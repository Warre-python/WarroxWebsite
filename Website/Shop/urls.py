from django.urls import path
from .views import shop, product, add_to_cart

urlpatterns = [
    path('', shop),
    path('<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]