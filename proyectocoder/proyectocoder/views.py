from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
def nacimiento(request, edad):
    edad=int(edad)
    anio=datetime.now().year-edad
    return HttpResponse(f"Nació en {anio}")

def vista_plantilla(request):
    archivo=open("C:/Users/juanc/Desktop/DJANGO/proyectocoder/proyectocoder/templates/plantilla_bonita.html")

    plantilla=Template(archivo.read())

    archivo.close()

    contexto= Context()

    documento=plantilla.render(contexto)
    
    return HttpResponse(documento)