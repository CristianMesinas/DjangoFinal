from django.contrib import admin
from django.urls import path
from inventarioF.views import listado, crearProducto, editarProducto, eliminarProducto

#para cargar configuracion css
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',listado, name= 'base'),
    path('crear/',crearProducto, name= 'crear'),        #name es la forma en la que lo identificamos dentro del codigo de URL
    path('editar/<id>',editarProducto, name='editar'),      #los path crear editar y eliminar corresponden a los propios botones para redireccionarnos a dichas url
    path('eliminar/<id>',eliminarProducto, name='eliminar') #los <id> son para indicar que van a estar recibiendo un id para poder eliminar/editar un determinado producto
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
#el + static se carga al final para que en ningun momento deje de funcionar los cambios en css