from django.forms import ModelForm
from .models import Cliente
from .models import Servico

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'        

       