from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Book
from.forms import BookForm


def books_list(request):
    books = models.Book.objects.all()
    context = {'books':books}
    return render(request, 'books_list.html', context)

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'books_detail.html', context)

def  new_book(request):
    if request.method == 'POST':
        #gusradr nuevo book
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/books')
    else:
        #ir al formulario
        form = BookForm()
        return render(request, 'new_book.html', {'form': form})
    
def edit_book(request, pk):
    book = Book.objects.get(pk = pk)
    form = BookForm(request.POST, instance = book)
    if form.is_valid():
        form.save()
        return redirect('/books')
    return render(request, 'edit_book.html', {'book': book})

def destroy(request, pk):
    book = Book.objects.get(pk = pk)
    book.delete()
    return redirect('/books')
    