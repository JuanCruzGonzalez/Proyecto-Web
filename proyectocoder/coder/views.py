from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Cursos(request):
    return render(request, "coder/cursos.html")

def Inicio(request):
    return render(request, "coder/inicio.html")

def Estudiantes(request):
    return render(request, "coder/estudiantes.html")

def Profesores(request):
    return render(request, "coder/profesores.html")

def Entregables(request):
    return render(request, "coder/entregables.html")