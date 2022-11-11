from django.urls import path
from coder.views import *
urlpatterns = {
    path("inicio/", Inicio),
    path("estudiantes/", Estudiantes),
    path("profesores/", Profesores),
    path("eursos/", Cursos),
    path("entregables/", Entregables),
}