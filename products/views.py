from django.shortcuts import render, redirect
# from django.views.decorators.cache import cache_page
from django.conf import settings

from products.models import Product
from products.forms import ProductModelForm

# Create your views here.

# @cache_page(settings.CACHE_TTL)
def list_products(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/list.html', context=context)

def create_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductModelForm()

    context = {
        'form': form
    }
    return render(request, 'products/create.html', context=context)

def update_product(request, product_id):
    search_product_id = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ProductModelForm(data=request.POST, instance=search_product_id)
        
        if form.is_valid():
            form.save()
            return redirect('products:list')

    else:
        form = ProductModelForm(instance=search_product_id)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']

            product_updated = Product(name=name,
                                      description=description,
                                      price=price,
                                      category=category)
                                      
            Product(product_updated)

    context = {
        'form': form,
    }

    return render(request, 'products/create.html', context=context)

def delete_product(request, product_id):
    search_product_id = Product.objects.get(pk=product_id)
    search_product_id.delete()
    
    return redirect('products:list')