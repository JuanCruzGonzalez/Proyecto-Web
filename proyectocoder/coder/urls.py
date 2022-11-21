from django.urls import path
from coder.views import *
urlpatterns =[
    path("inicio/", Inicio, name="coder-inicio"),
    path("estudiantes/", Estudiantes, name="coder-estudiantes"),
    path("profesores/", Profesores, name="coder-profesores"),
    path("cursos/", Cursos, name="coder-cursos"),
    path("cursos/actualizar/<id>", editar_curso, name="coder-cursos-editar"),
    path("entregables/", Entregables, name="coder-entregables"),
    path("formulario/curso", creacion_curso, name="creacion-curso"),
    path("formulario/profesores", creacion_profesores, name="formulario-profesores"),
    path("buscar/cursos", buscar_curso, name="cursos-buscar"),
    path("buscar/cursos/resultado", resultado_buscar_curso, name="cursos-buscar-resultado"),

    path('cursos/list/', CursoLista.as_view(), name="coder-cursos-list"),
    path('cursos/detalle/<pk>', CursoDetalle.as_view(), name="coder-cursos-detalle"),
    path('cursos/actualizar/<pk>', CursoUpdate.as_view(), name="coder-cursos-update"),
    path('cursos/crear/', CursoCrear.as_view(), name="coder-cursos-crear"),
    path('cursos/borrar/<pk>', CursoBorrar.as_view(), name="coder-cursos-borrar"),
]