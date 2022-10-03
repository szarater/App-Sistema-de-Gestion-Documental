from django.http import HttpResponse
from django.shortcuts import render
from sistemaGestionDocumental.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from sistemaGestionDocumental.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')

def buscar(request):
    if request.GET['prd']:
        #mensaje='Articulo buscado: %r' %request.GET['prd']
        producto=request.GET['prd']
        if len(producto)>20:
            mensaje='Texto de busqueda demasiado largo'
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultados_busqueda.html', {'articulos':articulos, 'query':producto})

    else:
        mensaje='No has introducido un requerimiento'
    return HttpResponse(mensaje)

def contacto(request):

    if request.method=='POST':
        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'],
            infForm.get('email', ''),['xxxxxx@gmail.com'],)

            return render(request, 'gracias.html')

    else:
        miFormulario=FormularioContacto()

    return render(request, 'formulario_contacto.html', {'form':miFormulario})