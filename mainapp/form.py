from django import forms
from django.forms import ModelForm
#from .models import Contact

class searchForm(forms.Form):

    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form__searchField'}))
    

