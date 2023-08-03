from django.shortcuts import render, redirect #hay que importar los distintos metodos a utilizar, de lo contrario no los reconoce
from django.http import HttpResponse
from .models import Productos, Categorias

# Create your views here.
def listado(request):
    productos = Productos.objects.all() #trae todos los productos
    categoria = Categorias.objects.all() #todos los objetos de Categorias se cargan en categoria
    context = {"productos": productos, "categorias":categoria} # con el context le decimos a django como representar mis productos y categorias en HTML
    return render(request, 'listado.html', context)

def crearProducto(request): # creamos el identificador para poder cargar nuevos datos
    nombre1 = request.POST ["nombre"] # "nombre" es tomado del ID usado en el modal para identificar que dato vamos a cargar
    precio1 = request.POST ["precio"] # "precio" es tomado del ID usado en el modal para identificar que dato vamos a cargar
    stock1 = request.POST ["stock"]
    categoria1 = request.POST ["categoria"]
    catego = Categorias.objects.get(id= categoria1) #traiga el objeto que selecciono en el select
    producto = Productos(nombre= nombre1, precio = precio1, stock = stock1, categoria = catego) #Nombre Precio y Stock provienen del models.py
    producto.save() #el .save se utiliza para guardar el producto en mi base de datos
    return redirect('/') #el redirect cuando se hace un return permite redireccionar
                         #a la url que se le indique en este caso la BASE

def editarProducto(request, id): #los id son para referenciar que producto editar/eliminar
#se puede poner tambien id_producto o prod_id o de la forma que queramos
#el id tambien hay que indicarlo en urls.py, y tiene que estar escrito exactamente igual
    producto = Productos.objects.get(id=id) #busca el producto que va a actualizar
    
    if request.method == 'GET': #metodo get es lo que ocurre cuando le damos click a editar al producto
        context = {'producto': producto}
        return render (request, 'editar.html', context)
    
    elif request.method == 'POST': #metodo post es lo que ocurre cuando le damos aceptar despues de editar el producto
        nuevo_nombre = request.POST ["nombre"] #obtiene los nuevos datos del producto
        nuevo_precio = request.POST ["precio"]
        nuevo_stock = request.POST ["stock"] 
        producto.nombre = nuevo_nombre #los reemplaza por los datos anteriores del producto
        producto.precio = nuevo_precio
        producto.stock = nuevo_stock
        producto.save() #el .save se utiliza para guardar los nuevos datos del producto en mi base de datos
        return redirect ("/")

def eliminarProducto(request, id): 
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('/')
    #return HttpResponse(f"se elimino el producto {producto.nombre}") 
    #el httpResponse es para mostrar mensajes en pantalla
    #return redirect es para cuando finaliza el proceso, te redireccione a la pagina especificada