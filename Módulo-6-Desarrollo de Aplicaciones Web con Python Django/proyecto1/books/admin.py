from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial')

admin.site.register(Book, BookAdmin)
