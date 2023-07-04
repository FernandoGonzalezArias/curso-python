from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    type = forms.CharField(widget=forms.RadioSelect(choices=Book.TIPOS_BOOK))
    class Meta:
        model = Book
        fields = ('titulo', 'editorial', 'state', 'type')