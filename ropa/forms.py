from django import forms

class PrendaFormulario(forms.Form):
    nombre = forms.CharField(required= True, max_length=64)
    categoria = forms.CharField(required=True, max_length=64)
    precio = forms.IntegerField(required=True, max_value=100000)

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required= True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    email = forms.EmailField(required=True)