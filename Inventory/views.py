# Django
from django.shortcuts import render, redirect
from django.views import generic
# Models
from .models import Product

# Create your views here.


class HomeView(generic.ListView):
    model = Product
    template_name = 'home.html'


def new_product(request):
    product = Product.objects.create()
    product.name = request.POST['name']
    product.save()
    return redirect('inventory:home')


def add(request):
    product = Product.objects.get(id=request.POST['id'])
    product.add1()
    product.save()
    return redirect('inventory:home')


def sub(request):
    product = Product.objects.get(id=request.POST['id'])
    product.sub1()
    product.save()
    return redirect('inventory:home')


def delete(request):
    product = Product.objects.get(id=request.POST['id'])
    product.delete()
    return redirect('inventory:home')
