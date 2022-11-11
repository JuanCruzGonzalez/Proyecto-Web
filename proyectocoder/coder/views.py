from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Cursos(request):
    return HttpResponse("Estas Cursos")

def Inicio(request):
    return render(request, "coder/index.html")

def Estudiantes(request):
    return HttpResponse("Estas Estudiantes")

def Profesores(request):
    return HttpResponse("Estas Profesores")

def Entregables(request):
    return HttpResponse("Estas Entregables")