"""projeto_oficina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include  
from cliente import views
from cliente import views as views_registrado
from cliente import views as views_servico

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',views.lista_cliente, name='clientes'), 
    path('search_cliente/',views.filtra_cliente,name='search_cliente'),   
    path('<int:id_cliente>', views.detalhe_cliente,name='detalhe_cliente' ),
    path('servicos/<int:id_servico>', views_servico.detalhe_servico,name='detalhe_servico'),
    path('novo/', views.novo_cliente, name='novo_cliente'),
    path('novo/<int:id_cliente>',views.editar_cliente,name='editar_cliente'),
    path('servicos/',views_servico.lista_servicos, name='servicos'), 
    path('search_servico/',views_servico.filtra_servico ,name='search_servico'),    
    path('novo_servico/', views_servico.novo_servico, name='novo_servico'),
    path('novo_servico/<int:id_servico>', views_servico.editar_servico, name='editar_servico'),
    path('search_pgto/',views_servico.filtra_pgto ,name='search_pgto'), 
    path('accounts/', include('django.contrib.auth.urls')),
]
