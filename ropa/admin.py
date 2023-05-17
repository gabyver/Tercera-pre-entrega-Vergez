from django.contrib import admin

# Register your models here.
from ropa.models import Categoria, Prenda, Cliente

admin.site.register(Categoria)
admin.site.register(Prenda)
admin.site.register(Cliente)