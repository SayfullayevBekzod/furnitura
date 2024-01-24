from django.shortcuts import render
from .models import Home, Product, ProductList, Shop, Choose, Team, More
# Create your views here.

def main(request):
    home = Home.objects.all()
    product = Product.objects.all()
    pro = ProductList.objects.all()
    return render(request=request, template_name='main.html', context={'homes': home, 'products': product, 'pros': pro})

def shop(request):
    shop = Shop.objects.all()
    return render(request=request, template_name='shop.html', context={'shops': shop})

def about(request):
    choose = Choose.objects.all()
    team = Team.objects.all()
    return render(request=request, template_name='about.html', context={'chooses': choose, 'teams': team})

def services(request):
    return render(request=request, template_name='services.html', context={})

def more(request):
    more = More.objects.all()
    return render(request=request, template_name='more.html', context={'mores': more})

def cart(request):
    return render(request=request, template_name='cart.html', context={})