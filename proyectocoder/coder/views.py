from django.shortcuts import render
from django.http import HttpResponse
from coder.models import *
from coder.forms import *

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

def creacion_curso(request):
    if request.method=="POST":
        nombre_curso=request.POST["curso"]
        nombre_camada=int(request.POST["camada"])
        Curso= curso(nombre=nombre_curso, camada=nombre_camada)
        Curso.save()
    return render(request, "coder/curso_formulario.html")

def creacion_profesores(request):
    if request.method =="POST":
        formulario = FormularioProfesor(request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            profesor= profesores(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()

    formulario = FormularioProfesor()
    return render(request, "coder/formulario_profesores.html",{"formulario":formulario})

def buscar_curso(request):
    return render(request, "coder/busqueda_cursos.html")

def resultado_buscar_curso(request):
    nombre_curso=request.GET["nombre_curso"]
    cursos=curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "coder/resultado_buscar_curso.html", {"cursos":cursos})