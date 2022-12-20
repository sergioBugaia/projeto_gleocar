from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Pronto para cadastrar cliente !')

def clientes(request):
    pessoa = {
        'nome':'Sergio',
        'idade':56,
        'hobby':'python'
    }
    return render(request, 'oficina/clientes.html',pessoa)

# Create your views here.
