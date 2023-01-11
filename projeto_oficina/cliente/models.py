from django.db import models
from datetime import datetime


class Cliente(models.Model):
    cliente_nome = models.CharField(max_length=100)
    cliente_telefone = models.CharField(max_length=11,default=0)
    cliente_email = models.CharField(max_length=50,default=0)    
    def __str__(self):
        return self.cliente_nome

class Servico(models.Model):
    servico = models.TextField(max_length=255)
    fabricante = models.CharField(max_length=100,default=0)
    modelo = models.CharField(max_length=100,default=0)
    ano_fab = models.CharField(max_length=4,default=0)
    cor = models.CharField(max_length=50,default=0)
    placa = models.CharField(max_length=7,default=0)
    valor = models.DecimalField('valor',max_digits=8,decimal_places=2,null=True,default=0.0)
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.servico

    class Meta:
        ordering = ['data']       




