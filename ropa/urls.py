from django.contrib import admin
from django.urls import path

from ropa.views import crear_prendas, buscar_prendas

urlpatterns = [
    path("prendas/", crear_prendas),
    path("buscar_prendas", buscar_prendas),
]
