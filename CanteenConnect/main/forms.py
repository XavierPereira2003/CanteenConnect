from django import forms
from django.forms import ModelForm
from .models import Menu


#Form for chef input

class Menu_form(ModelForm):
    class Meta:
        model=Menu
        fields=('Date','item1','item2','item3','item4','item5')
