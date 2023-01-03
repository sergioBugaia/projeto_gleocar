from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Cliente
from .models import Servico

def pagina_inicial(request):
    return HttpResponse('Pronto para cadastrar cliente !')

def novo_cliente(request):
    return render(request, 'oficina/novo_cliente.html')

# def cliente_registrado(request):
#     customer = {
#         'new_customer':request.POST.get('New_customer')
#     }
#     return render(request,'oficina/cliente_registrado.html',customer)

def lista_cliente(request):
    dados_cliente = {
        'dados_cliente':Cliente.objects.all().order_by('-servico')
    }
    return render(request,'oficina/clientes.html',context=dados_cliente)

def detalhe_cliente(request, id_cliente):
    dados_cliente = {
        'dados_cliente':Cliente.objects.get(pk=id_cliente)
    }
    return render(request, 'oficina/detalhe.html',dados_cliente)

def lista_servicos(request):
    dados_servico = {
        'dados_servico':Servico.objects.select_related('cliente').order_by('-data')
    }
    return render(request,'oficina/servicos.html',context=dados_servico)

def detalhe_servico(request,id_servico):
    dados_servico = {
       'dados_servico':Servico.objects.get(pk=id_servico)
        
    }
    return render(request, 'oficina/detalhe_servico.html', dados_servico)



