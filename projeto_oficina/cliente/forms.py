from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator
from .models import Cliente
from .models import Servico

#capitalize
#def clean(self):
#   self.cliente_nome = self.cliente_nome.capitalize()    

#letters to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower() 

#letters to upercase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()         

class ClienteForm(forms.ModelForm):
    #VALIDATIONS
    cliente_nome = Uppercase(
        label='Nome',min_length=3, max_length=100,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Use somente letras")],
        widget=forms.TextInput(attrs={'placeholder': 'Nome e sobrenome'})
    )

    cliente_telefone = forms.CharField(
        label='Telefone',min_length=11, max_length=13 ,
        validators= [RegexValidator(r'^[0-9\s-]*$',message="Use o modelo 43-99999-9999")],
        widget=forms.TextInput(attrs={'placeholder': '43-99999-9999'})
    )

    cliente_email = Lowercase(
        label='Email',min_length=8, max_length=50,
        validators= [RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message="Insira um Email válido")],
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = Cliente
        fields = '__all__'

class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'        

       