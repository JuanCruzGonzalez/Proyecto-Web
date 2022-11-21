from django import forms
class FormularioProfesor(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()