
from django import forms

class AlumnoFormulario(forms.Form):
     nombre = forms.CharField(required = True, max_length=255)
     apellido = forms.CharField(required = True, max_length=255)
class ArtemarcialFormulario(forms.Form):
    estilo = forms.CharField(max_length=255)
    pais = forms.CharField(max_length=255)
    zona = forms.CharField(max_length=128)

class PeliculaFormulario(forms.Form):
    titulo = forms.CharField(max_length=255)
    director = forms.CharField(max_length=255)
    duracion = forms.IntegerField()