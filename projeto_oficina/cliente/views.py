from django.shortcuts import render, redirect ,HttpResponse
from django.contrib.auth.decorators import login_required  
from .models import Cliente
from .models import Servico
from .forms import ClienteForm
from .forms import ServicoForm

@login_required
def novo_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('clientes')
        else:           
            formulario = {
                'formulario': cliente_form
            }
            return render(request, 'oficina/novo_cliente.html',context=formulario) 
    else:  
        cliente_form = ClienteForm()
        formulario = {
                'formulario': cliente_form
            }
        return render(request, 'oficina/novo_cliente.html',context=formulario) 

                         
 
@login_required
def lista_cliente(request):
    dados_cliente = {
        'dados_cliente':Cliente.objects.all().order_by('-servico')[:7]
    }
    return render(request,'oficina/clientes.html',context=dados_cliente)

@login_required
def filtra_cliente(request):
    if request.method == "POST":  
        searched = request.POST['searched']  
        clientes = Cliente.objects.filter(cliente_nome__icontains=searched)  
        return render(request,'oficina/search_cliente.html',{'searched':searched,'clientes':clientes})  
    else:
        return render(request,'oficina/clientes.html')           
@login_required
def detalhe_cliente(request, id_cliente):
    dados_cliente = {
        'dados_cliente':Cliente.objects.get(pk=id_cliente)
    }
    return render(request, 'oficina/detalhe.html',dados_cliente)

@login_required
def lista_servicos(request):
    dados_servico = {
        'dados_servico':Servico.objects.select_related('cliente').order_by('-data')[:7]
    }
    return render(request,'oficina/servicos.html',context=dados_servico)

@login_required
def filtra_servico(request):
    if request.method == "POST":  
        searched = request.POST['searched']  
        servicos = Servico.objects.filter(modelo__icontains=searched)  
        return render(request,'oficina/search_servico.html',{'searched':searched,'servicos':servicos})  
    else:
        return render(request,'oficina/servicos.html')

@login_required
def detalhe_servico(request,id_servico):
    dados_servico = {
       'dados_servico':Servico.objects.get(pk=id_servico)
        
    }
    return render(request, 'oficina/detalhe_servico.html', dados_servico)

@login_required
def novo_servico(request):
    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)
        if servico_form.is_valid():
            servico_form.save()
        return redirect('/servicos')
    else:    
        servico_form = ServicoForm()
        formulario = {
            'formulario_servico': servico_form
        }
        return render(request, 'oficina/novo_servico.html',context=formulario)

@login_required
def editar_cliente(request,id_cliente):
    cliente_edit = Cliente.objects.get(pk=id_cliente)
    if request.method == 'GET':
        formulario = ClienteForm(instance=cliente_edit)
        return render(request,'oficina/novo_cliente.html',{'formulario':formulario})
    else:
        formulario = ClienteForm(request.POST,instance=cliente_edit)        
        if formulario.is_valid():
            formulario.save()
        return redirect('clientes') 
        
@login_required
def editar_servico(request,id_servico):
    servico_edit = Servico.objects.get(pk=id_servico)
    if request.method == 'GET':
        formulario = ServicoForm(instance=servico_edit)        
        return render(request, 'oficina/novo_servico.html',{'formulario_servico':formulario})
    else:
        formulario = ServicoForm(request.POST,instance=servico_edit)
        if formulario.is_valid():
            formulario.save()
        return redirect('servicos')            


