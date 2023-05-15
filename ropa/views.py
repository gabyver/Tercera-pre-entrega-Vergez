from django.shortcuts import render

# Create your views here.
def agregar_prendas(request):
    if request.method == "POST":
        formulario = PrendaFormulario(request.POST)
        if formulario.is_valid():
            data =formulario.cleaned_data
            nombre = data["nombre"]
            categoria = data ["categoria"]
            precio = data ["precio"]
            descripcion = data ["descripcion"]
            prenda = Prenda
            prenda.save()
            url_exitosa = reverse ("lista_prendas")
            return redirect (url_exitosa)
        else:
            formulario = PrendaFormulario()
            http_responde = render(
                request = request,
                template_name = 'ropa/formulario_prenda.html'
                context ={'formulario': formulario}
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
            template_name='ropa/busca_clientes.html',
            context=contexto,
        )
        return http_response


def listar_prendas(request):
    contexto = {
        "prendas": Prenda.objects.all(),
    }
    http_response = render(
        request = request,
        template_name='ropa/lista_prendas.html',
        context=contexto,
    )
    return http_response
