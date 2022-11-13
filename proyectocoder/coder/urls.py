from django.urls import path
from coder.views import *
urlpatterns =[
    path("inicio/", Inicio, name="coder-inicio"),
    path("estudiantes/", Estudiantes, name="coder-estudiantes"),
    path("profesores/", Profesores, name="coder-profesores"),
    path("cursos/", Cursos, name="coder-cursos"),
    path("entregables/", Entregables, name="coder-entregables"),
    path("formulario/curso", creacion_curso, name="creacion-curso"),
    path("formulario/profesores", creacion_profesores, name="formulario-profesores"),
    path("buscar/cursos", buscar_curso, name="cursos-buscar"),
    path("buscar/cursos/resultado", resultado_buscar_curso, name="cursos-buscar-resultado"),
]