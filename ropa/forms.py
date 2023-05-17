from django import forms

class PrendaFormulario(forms.Form):
    nombre = forms.CharField(required= True, max_length=64)
    categoria = forms.CharField(required=True, max_length=64)
    precio = forms.IntegerField(required=True, max_value=100000)

