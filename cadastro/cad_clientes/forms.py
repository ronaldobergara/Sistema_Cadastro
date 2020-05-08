from django import forms
from django.core.exceptions import ValidationError


list_UF = [('', ''),('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), 
           ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), 
           ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ',), ('RN', 'RN'), ('RS', 'RS'), 
           ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')]

class CadClienteForm(forms.Form):
    cnpj            = forms.CharField(label='CNPJ:')
    razaoSocial     = forms.CharField(label='Razão Social:')   
    nomeFantasia    = forms.CharField(label='Nome Fantasia:')
    cep             = forms.CharField(label='CEP:')
    endereco        = forms.CharField(label='Endereço:')
    numero          = forms.CharField(label='Numero:')
    uf              = forms.ChoiceField(choices=list_UF,label='UF:')
    consumidorFinal = forms.BooleanField(label='Consumidor Final')
    # 