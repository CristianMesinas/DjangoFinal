from django.shortcuts import render, redirect #hay que importar los distintos metodos a utilizar, de lo contrario no los reconoce
from django.http import HttpResponse
from .models import Productos

# Create your views here.
def listado(request):
    productos = Productos.objects.all() #trae todos los productos
    context = {"productos": productos} # con el context le decimos a django como representar mis productos en HTML
    return render(request, 'listado.html', context)

def crearProducto(request): # creamos el identificador para poder cargar nuevos datos
    nombre1 = request.POST ["nombre"] # "nombre" es tomado del ID usado en el modal para identificar que dato vamos a cargar
    precio1 = request.POST ["precio"] # "precio" es tomado del ID usado en el modal para identificar que dato vamos a cargar
    stock1 = request.POST ["stock"] # "stock" es tomado del ID usado en el modal para identificar que dato vamos a cargar
    producto = Productos(nombre= nombre1, precio = precio1, stock = stock1) #Nombre Precio y Stock provienen del models.py
    producto.save() #el .save se utiliza para guardar el producto en mi base de datos
    return redirect('/') #el redirect cuando se hace un return permite redireccionar
                         #a la url que se le indique en este caso la BASE