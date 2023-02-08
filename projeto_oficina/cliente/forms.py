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
        widget=forms.TextInput(attrs={'placeholder': 'Nome e sobrenome','autofocus':True})
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
     #VALIDATIONS
    servico = Uppercase(
        label='Descrição',min_length=5, max_length=255,
        widget=forms.Textarea (attrs={'autofocus':True})
    )

    fabricante = Uppercase(
        label='Fabricante',min_length=2, max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Use somente letras")],
        widget=forms.TextInput(attrs={'placeholder': 'Nome e sobrenome'})
    )

    modelo = Uppercase(
        label='Modelo',min_length=3, max_length=50,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Use somente letras")],
        widget=forms.TextInput(attrs={'placeholder': 'Nome e sobrenome'})
    )

    ano_fab = forms.CharField(
        label='Ano Veiculo',min_length=4, max_length=9 ,
        validators= [RegexValidator(r'^[0-9\s-]*$',message="Use o modelo 2022-2022")],
        widget=forms.TextInput(attrs={'placeholder': '2022-2022'})
    )

    cor = Uppercase(
        label='Cor Veiculo',min_length=3, max_length=15,
        validators= [RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',message="Use somente letras")],
        widget=forms.TextInput(attrs={'placeholder': 'Cor'})
    )

    placa = Uppercase(
        label='Placa',min_length=7, max_length=8 ,
        validators= [RegexValidator(r'^[a-zA-Z0-9\s-]*$',message="Use o modelo ABC-1234")],
        widget=forms.TextInput(attrs={'placeholder': 'ABC-1234'})
    )

    valor = forms.CharField(
        label='Valor',min_length=3, max_length=10 ,
        validators= [RegexValidator(r'(?:\.|,|[0-9])*', message="Use o modelo 10.000,00")],        
        widget=forms.TextInput(attrs={'placeholder': '10.000,00'})
    )

    
    
    class Meta:
        model = Servico
        fields = '__all__'        

       