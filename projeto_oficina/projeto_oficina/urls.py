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
from cliente import views
from cliente import views as views_registrado
from cliente import views as views_servico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.lista_cliente),
    path('/<int:id_cliente>', views.detalhe_cliente,name='detalhe' ),
    path('novo/', views.novo_cliente, name='novo_cliente'),
    path('servicos/',views.lista_servicos, name='servicos'),
    #path('registrado/', views_registrado.cliente_registrado, name='cliente_registrado'),    
]
