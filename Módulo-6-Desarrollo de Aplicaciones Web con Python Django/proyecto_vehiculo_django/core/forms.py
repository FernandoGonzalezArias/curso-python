from bootstrap5.widgets import RadioSelectButtonGroup
from django import forms

class MyForm(forms.Form):
    media_type = forms.ChoiceField(
        help_text = "selected the prder type.",
        required = True,
        label= "Order Type:",
        widget = RadioSelectButtonGroup,
        choices = ((1, 'Vinyl'), (2,'Compact Disc')),
        initial = 1,
    )
    
    name = forms.CharField(max_length=100)
    
    class Meta:
        fields = ('madia_type', 'name')