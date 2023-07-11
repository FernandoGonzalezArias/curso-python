from django.shortcuts import render
from django.contrib import messages
from .forms import MyForm

def home ( request):
    return render(request, "home.html", context={})

def contact(request):
    messages.warning(request, " esto es un test")
    form = MyForm()
    return render(request, "contact.html", context={'form': form})
