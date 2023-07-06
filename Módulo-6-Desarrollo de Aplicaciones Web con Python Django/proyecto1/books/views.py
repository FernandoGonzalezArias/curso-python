from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from .models import Book
from.forms import BookForm
from django.contrib import messages
import sweetify


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
        #guardar nuevo book
        values = request.POST.getlist('favorite_color')
        colors = ",".join(values)
        editorial = request.POST['editorial']
        state = request.POST['state']
        type_form = request.POST['type']
        titulo = request.POST['titulo']
        obj1 = Book(
            editorial = editorial,
            state = state,
            type = type_form,
            favorite_color = colors,
            titulo = titulo
        )
        obj1.save()
        sweetify.success(request, 'El libro se creo correctamente')
        return redirect('/books')
    else:
        #ir al formularios
        form = BookForm()
        return render(request, 'new_book.html', {'form': form})
    
def edit_book(request, pk):
    book = Book.objects.get(pk = pk)
    if book.favorite_color != "":
       selected_colors = book.favorite_color.split(",")
    else:
        selected_colors = []
        
    selected_colors = [int(x) for x in selected_colors]
    if request.method == 'POST':
        editorial = request.POST['editorial']
        state = request.POST['state']
        type_form = request.POST['type']
        titulo = request.POST['titulo']
        values = request.POST.getlist('favorite_color')
        colors = ",".join(values)
        book.editorial = editorial
        book.state = state
        book.type = type_form
        book.titulo = titulo
        book.favorite_color = colors
        book.save()
        sweetify.toast(request, 'El libro se edito correctamente', icon="success", timer=3000)
        return redirect('/books')
    return render(request, 'edit_book.html', {'book': book, 'states': Book.STATUS, 'type': Book.TIPOS_BOOK, 'colors':Book.COLORS, 'selected_colors':selected_colors})

def destroy(request, pk):
    book = Book.objects.get(pk = pk)
    book.delete()
    sweetify.toast(request, 'El libro se elimino correctamente', icon="success", timer=3000)
    return redirect('/books')
    