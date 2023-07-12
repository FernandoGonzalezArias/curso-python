from django.shortcuts import render
from .forms import ProductsForm, AddressForm

def new(request):
    form = ProductsForm()
    return render(request, "products/new.html", context={'form': form})

def new_address(request):
    form = AddressForm()
    return render(request, "products/new_address.html", context={'form': form})


