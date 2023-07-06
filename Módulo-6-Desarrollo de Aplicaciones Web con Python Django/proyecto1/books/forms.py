from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    type = forms.CharField(widget=forms.RadioSelect(choices=Book.TIPOS_BOOK))
    favorite_color = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=Book.COLORS))
    class Meta:
        model = Book
        fields = ('titulo', 'editorial', 'state', 'type', 'favorite_color')