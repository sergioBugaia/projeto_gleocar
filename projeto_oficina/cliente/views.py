from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Cliente

def pagina_inicial(request):
    return HttpResponse('Pronto para cadastrar cliente !')

def novo_cliente(request):
    return render(request, 'oficina/novo_cliente.html')

def cliente_registrado(request):
    customer = {
        'new_customer':request.POST.get('New_customer')
    }
    return render(request,'oficina/cliente_registrado.html',customer)

def lista_cliente(request):
    dados = {
        'dados':Cliente.objects.all()
    }
    return render(request,'oficina/clientes.html',context=dados)



