from django.shortcuts import render

def new(request):
    return render(request, "products/new.html", context={})
