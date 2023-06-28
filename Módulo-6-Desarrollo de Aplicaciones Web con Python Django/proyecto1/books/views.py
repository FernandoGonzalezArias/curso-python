from django.shortcuts import render
from . import models


def books_list(request):
    books = models.Book.objects.all()
    context = {'books':books}
    return render(request, 'books_list.html', context)
