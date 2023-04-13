from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def admin(request):
    if request.method == 'POST':
        name = request.POST['name']
        product = Product.objects.create(name=name)
        product.save()
    products = Product.objects.all()
    return render(request, 'admin.html', {'products': products})

def product_manager(request):
    products = Product.objects.all()
    return render(request, 'product_manager.html', {'products': products})