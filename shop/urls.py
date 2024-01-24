from django.urls import path
from .views import main, shop, about, services, more, cart

urlpatterns = [
    path('', main, name='main'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('more/', more, name='more'),
    path('cart/', cart, name='cart'),
]