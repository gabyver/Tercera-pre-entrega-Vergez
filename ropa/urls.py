from django.contrib import admin
from django.urls import path

from ropa.views import crear_prendas, buscar_prendas, listar_prendas, crear_clientes, buscar_clientes, listar_clientes

urlpatterns = [
    path("prendas/", crear_prendas),
    path("buscar_prendas/", buscar_prendas),
    path("listar_prendas/", listar_prendas, name="lista_prenda"),
    path("clientes/", crear_clientes),
    path("buscar_clientes/", buscar_clientes),
    path("listar_clientes/", listar_clientes, name="lista_cliente"),
    
]
