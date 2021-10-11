from django import forms
from django.forms import ModelForm
#from .models import Contact

class contactForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form__field'}))
    
# Formulario contacto 300921
class FormularioContacto (forms.Form):
    nombreForm = forms.CharField(max_length=50)
    apellidoForm = forms.CharField(max_length=50)
    email_direcc = forms.EmailField(max_length=150)
    mensaje = forms.CharField(widget= forms.Textarea, max_length=2000)

    