"""proyectocoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from proyectocoder.views import *
from coder.views import *
import proyectocoder.settings as settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("nacimiento/<edad>/", nacimiento),
    path("plantilla/", vista_plantilla),
    path("alumnos/", vista_listado_alumnos2),
    path("coder/", include("coder.urls")),
    path("", Inicio, name="coder-inicio"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)