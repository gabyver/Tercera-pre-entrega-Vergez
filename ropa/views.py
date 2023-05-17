from django.shortcuts import render
fron django.urls import reverse
from tienda_ropa.models import Prenda, Cliente

# Create your views here.
def inicio(request):
    contexto= {}
    http_response = render(
        request=request,
        template_name= 'tienda_ropa/index.html',
        context=contexto,
    )
    return http_response

def crear_prendas(request):
    if request.method == "POST":
        formulario = PrendaFormulario(request.POST)
        if formulario.is_valid():
            data =formulario.cleaned_data
            nombre = data["nombre"]
            categoria = data ["categoria"]
            precio = data ["precio"]
            prenda = Prenda.objects.create(nombre=nombre, categoria=categoria, precio=precio)
            url_exitosa = reverse ("lista_prenda")
            return redirect (url_exitosa)
        else:
            formulario = PrendaFormulario()
            http_responde = render(
                request = request,
                template_name = 'ropa/formulario_prenda.html',
                context ={'formulario': formulario},
            )
            return http_responde
        
        
def buscar_prendas(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        prendas = Prenda.objects.filter(prenda__icontains=busqueda)
        contexto = {
            "prendas": prendas,
        }
        http_response= render(
            request = request,
            template_name='ropa/busca_prenda.html',
            context=contexto,
        )
        return http_response


def listar_prendas(request):
    contexto = {
        "prendas": Prenda.objects.all(),
    }
    http_response = render(
        request = request,
        template_name='ropa/lista_prenda.html',
        context=contexto,
    )
    return http_response


def crear_clientes(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            data =formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data ["apellido"]
            email = data ["email"]
            cliente = Cliente.objects.create(nombre=nombre, apellido=apellido, email=email)
            url_exitosa = reverse ("lista_cliente")
            return redirect (url_exitosa)
        else:
            formulario = ClienteFormulario()
            http_responde = render(
                request = request,
                template_name = 'ropa/formulario_cliente.html',
                context ={'formulario': formulario},
            )
            return http_responde
        
        
def buscar_clientes(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        clientes = Cliente.objects.filter(cliente__icontains=busqueda)
        contexto = {
            "clientes": clientes,
        }
        http_response= render(
            request = request,
            template_name='ropa/busca_cliente.html',
            context=contexto,
        )
        return http_response
    
def listar_clientes(request):
    contexto = {
        "clientes": Cliente.objects.all(),
    }
    http_response = render(
        request = request,
        template_name='ropa/lista_cliente.html',
        context=contexto,
    )
    return http_response
