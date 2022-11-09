from django.forms import ModelForm
from .models import Investimento #importação das tabelas do DB

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__' # para exibir todos os campos