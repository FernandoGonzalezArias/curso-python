from django import forms
from .models import Product


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=('name', 'description')
        
class AddressForm(forms.Form):
    STATES = (
        ('RM', 'Region Metropolitana'),
        ('V', 'Quinta Region'),
        ('VII', 'Octava Region'),
    )
    
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Introduce un email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 50}))
    state = forms.ChoiceField(choices=STATES, initial='V')
    check_me = forms.BooleanField()