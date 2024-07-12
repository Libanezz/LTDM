from django.shortcuts import render
from .models import ProductosTiendita, Categoria

# Create your views here.

def index(request):
    return render (request, 'productosApp/index.html')

def login(request):
    return render(request, 'productosApp/login.html')

def registro(request):
    return render(request, 'productosApp/registro.html')

def ropadehombre(request):
    productos=ProductosTiendita.objects.filter(id_categoria=1)
    context={'productos' : productos}
    return render(request, 'productosApp/ropadehombre.html', context)

def ropademujer(request):
    productos=ProductosTiendita.objects.filter(id_categoria=2)
    print(productos)  # Esto imprimirá en la consola los productos recuperados
    context={'productos' : productos}
    return render(request, 'productosApp/ropademujer.html', context)

def joyeria(request):
    productos=ProductosTiendita.objects.filter(id_categoria=3)
    context={'productos' : productos}
    return render(request, 'productosApp/joyeria.html', context)





