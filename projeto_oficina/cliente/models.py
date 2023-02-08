from django.db import models
from datetime import datetime


class Cliente(models.Model):
    cliente_nome = models.CharField(max_length=100)
    cliente_telefone = models.CharField(max_length=13)
    cliente_email = models.CharField(max_length=50)    
    def __str__(self):
        return self.cliente_nome

class Servico(models.Model):
    servico = models.TextField(max_length=255)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fab = models.CharField(max_length=4)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    valor = models.CharField(max_length=12)
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.servico

    class Meta:
        ordering = ['data']       




