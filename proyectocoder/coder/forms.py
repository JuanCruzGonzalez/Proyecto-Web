from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioProfesor(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class UserRegitrerForm(UserCreationForm):
    email=forms.EmailField(label="Correo electronico")
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido")
    class Meta():
        model=User
        fields = ["username", "email", "last_name", "password1", "password2"]
    
class UserEditForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la Contraseña", widget=forms.PasswordInput)
    email=forms.EmailField(label="Correo electronico")
    last_name = forms.CharField(label="Apellido")
    class Meta():
        model=User
        fields = ["email", "last_name"]
        help_texts = {k: "" for k in fields}
    
class AvatarForm(forms.Form):
    imagen= forms.ImageField()

