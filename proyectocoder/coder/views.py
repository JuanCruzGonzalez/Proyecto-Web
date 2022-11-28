from django.shortcuts import render, redirect
from django.http import HttpResponse
from coder.models import *
from coder.forms import *
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
    if request.user.is_authenticated:
        imagen_model=Avatar.objects.filter(user=request.user.id).order_by("-id")[0]
        imagen_url= imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "coder/inicio.html", {"imagen_url": imagen_url})

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
            return render(request, "coder/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})
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

class CursoLista(LoginRequiredMixin, ListView):
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

def login_user(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("coder-inicio")
            else:
                return render(request, "coder/login.html", {"formulario": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "coder/login.html", {"formulario": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "coder/login.html", {"formulario": formulario, "errors": errors})

def registrar_usuario(request):

    if request.method=="POST":
        formulario=UserRegitrerForm(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            return redirect("coder-inicio")
        else:
            return render(request, 'coder/register.html', {"formulario":formulario,"errors": formulario.errors})
    
    formulario = UserRegitrerForm()
    return render(request, 'coder/register.html', {"formulario":formulario})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        # * cargar informacion en el formulario
        formulario=UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
        # ! validacion del formulario
        # * actualizacion del usuario con los datos del formulario
            usuario.email = data["email"]
            usuario.last_name = data["last_name"]
            
            usuario.save()
            return redirect('coder/inicio.html')
    else:
        # * crear formulario vacio
        return render(request, 'coder/modificar_perfil.html', {"form": formulario, "errors": formulario.errors})
    return render(request, "coder/modificar_perfil.html", {"form": formulario})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        # * cargar informacion en el formulario
        formulario = UserEditForm(request.POST)

        # ! validacion del formulario
        if formulario.is_valid():
            data = formulario.cleaned_data

            # * actualizacion del usuario con los datos del formulario
            usuario.email = data["email"]
            usuario.first_name = data["first_name"]

            usuario.save()
            return redirect("coder-inicio")
        else:
            return render(request, "coder/editar_perfil.html", {"form": formulario, "erros": formulario.errors})
    else:
        # * crear formulario vacio
        formulario = UserEditForm(initial = {"email": usuario.email, "last_name": usuario.last_name})

    return render(request, "coder/modificar_perfil.html", {"form": formulario})

@login_required
def avatar(request):
    if request.method=="POST":

        formulario= AvatarForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            data=formulario.cleaned_data

            usuario=request.user

            avatar=Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("coder-inicio")
        
        else:
            return render(request, 'coder/agregar_avatar.html',{"form":formulario, "errors":formulario.errors})

    formulario= AvatarForm()

    return render(request, 'coder/agregar_avatar.html',{"form":formulario} )
