from django.urls import path
from .views import home, terminal

urlpatterns = [
    path('', home),
    path('terminal/', terminal, name='terminal'),
]
