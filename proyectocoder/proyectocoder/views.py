from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
def nacimiento(request, edad):
    edad=int(edad)
    anio=datetime.now().year-edad
    return HttpResponse(f"Nació en {anio}")

def vista_plantilla(request):
    archivo=open("C:/Users/juanc/Desktop/DJANGO/proyectocoder/proyectocoder/templates/plantilla_bonita.html")

    plantilla=Template(archivo.read())

    archivo.close()

    datos={"nombre": "Juan", "Fecha": datetime.now(), "Apellido":"Gonzalez"}

    contexto= Context(datos)

    documento=plantilla.render(contexto)
    
    return HttpResponse(documento)

def vista_listado_alumnos(resquest):
    archivo=open(r"C:\Users\juanc\Desktop\DJANGO\proyectocoder\proyectocoder\templates\listado_alumnos.html")

    plantilla=Template(archivo.read())

    archivo.close()

    listado_alumnos=["JUAN GONZALEZ", "LEONEL GAREIS", "SANTIAGO ORTIZ", "LUCAS PIOVILLICO"]
    datos={"Tecnologia":"Python", "listado_alumnos": listado_alumnos}
    
    contexto=Context(datos)

    documento=plantilla.render(contexto)

    return HttpResponse(documento)

def vista_listado_alumnos2(request):
    listado_alumnos=["JUAN GONZALEZ", "LEONEL GAREIS", "SANTIAGO ORTIZ", "LUCAS PIOVILLICO"]
    datos={"Tecnologia":"Python", "listado_alumnos": listado_alumnos}
    plantilla=loader.get_template("base.html")
    documento=plantilla.render(datos)
    return HttpResponse(documento)