from django.shortcuts import render, redirect
from django.http import HttpResponse
from coder.models import *
from coder.forms import *
from django.views.generic import *

# Create your views here.
def Cursos(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso=Curso(nombre=data["nombre"], camada=data["camada"])
            curso.save()
        else:
            errores=formulario.errors

    curses=Curso.objects.all()
    formulario=CursoFormulario()
    contexto={"listado_cursos":curses, "formulario":formulario}

    return render(request, "coder/cursos.html", contexto)

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
        curso= Curso(nombre=nombre_curso, camada=nombre_camada)
        curso.save()
    return render(request, "coder/curso_formulario.html")

def borrar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('coder-cursos')

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save()
            return redirect("coder-cursos")
        else:
            return render(request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})
        return render(request, "coder/editar_curso.html", {"formulario": formulario, "errores": ""})

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
    cursos=Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "coder/resultado_buscar_curso.html", {"cursos":cursos})

class CursoLista(ListView):
    model = Curso
    template_name = 'coder/curso_list.html'

class CursoDetalle(DetailView):
    model = Curso
    template_name = 'coder/curso_detalle.html'

class CursoCrear(CreateView):
    model = Curso
    success_url = '/coder/cursos.html'
    fields = ['camada', 'nombre']

class CursoUpdate(UpdateView):
    model= Curso
    success_url = '/coder/cursos.html'
    fields = ['camada', 'nombre']

class CursoBorrar(DeleteView):
    model= Curso
    success_url = 'coder/cursos.html'