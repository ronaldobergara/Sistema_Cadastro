from django import forms
from django.core.exceptions import ValidationError
from cadastro.cad_clientes.models import CadCliente

# Personalisar mensagem de erro para todos os campos
REQUIRED = dict(required=('Campo Obrigatório'))

class CadClienteFormOld(forms.Form):
    cnpj            = forms.CharField(label='CNPJ:')
    razaoSocial     = forms.CharField(label='Razão Social:')   
    nomeFantasia    = forms.CharField(label='Nome Fantasia:')
    cep             = forms.CharField(label='CEP:')
    endereco        = forms.CharField(label='Endereço:', required=True)
    numero          = forms.CharField(label='Numero:')
    uf              = forms.ChoiceField(label='UF:')
    consumidorFinal = forms.BooleanField(label='Consumidor Final', required=False)
    # 

class CadClienteForm(forms.ModelForm):
   # uf = forms.ChoiceField(choices=list_UF,label='UF:')
    class Meta:
        model = CadCliente
        fields = ['cnpj', 'razaoSocial', 'nomeFantasia', 'cep', 'endereco', 'numero', 'uf', 'consumidorFinal']
        error_messages = {f.name: REQUIRED for f in  CadCliente._meta.fields} # Personalisar mensagem de erro para todos os campos