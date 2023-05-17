from django.contrib import admin
from django.urls import path

from ropa.views import crear_prendas, buscar_prendas, listar_prendas, buscar_clientes, listar_clientes

urlpatterns = [
    path("prendas/", crear_prendas),
    path("buscar_prendas", buscar_prendas),
    path("listar_prendas", listar_prendas),
    path("buscar_clientes", buscar_clientes),
    path("listar_clientes", listar_clientes),
]
