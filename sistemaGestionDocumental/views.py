from django.http import HttpResponse
from django.shortcuts import render
from sistemaGestionDocumental.models import Articulos

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')

def buscar(request):
    if request.GET['prd']:
        #mensaje='Articulo buscado: %r' %request.GET['prd']
        producto=request.GET['prd']
        articulos=Articulos.objects.filter(nombre__icontains=producto)
        return render(request, 'resultados_busqueda.html', {'articulos':articulos, 'query':producto})

    else:
        mensaje='No has introducido un requerimiento'
        return HttpResponse(mensaje)
