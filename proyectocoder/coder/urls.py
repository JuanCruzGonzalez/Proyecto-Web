from django.urls import path
from coder.views import *
urlpatterns =[
    path("inicio/", Inicio, name="coder-inicio"),
    path("estudiantes/", Estudiantes, name="coder-estudiantes"),
    path("profesores/", Profesores, name="coder-profesores"),
    path("cursos/", Cursos, name="coder-cursos"),
    path("entregables/", Entregables, name="coder-entregables"),
]