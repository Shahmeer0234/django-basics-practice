from django import forms

from django.forms.widgets import NumberInput

Favourite_Dish = [
    ('italian','Italian'),
    ('greek', 'Greek'),
    ('turkish', 'Turkish')
]


class DemoForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(required=True, label='Your Email')
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    favourite_dish = forms.ChoiceField(widget=forms.RadioSelect, choices=Favourite_Dish)