from django.shortcuts import render
from .forms import ProductsForm

def new(request):
    form = ProductsForm()
    return render(request, "products/new.html", context={'form': form})
