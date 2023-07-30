from django.contrib import admin
from django.urls import path
from inventarioF.views import listado, crearProducto


urlpatterns = [
    path('',listado),
    path('crear/',crearProducto, name= 'crear'), #name es la forma en la que lo identificamos dentro del codigo de URL
]