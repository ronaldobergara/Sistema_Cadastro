from django.db import models

list_UF = [('', ''),('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), 
           ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), 
           ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ',), ('RN', 'RN'), ('RS', 'RS'), 
           ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')]

# Create your models here.
class CadCliente(models.Model):
    razaoSocial     = models.CharField('Razão Social', max_length=150)   
    nomeFantasia    = models.CharField('Nome Fantasia', max_length=100)
    cep             = models.CharField('CEP', max_length=8)
    endereco        = models.CharField('Endereço', max_length=200)
    numero          = models.CharField('Numero', max_length=10)
    uf              = models.CharField('UF', max_length=2, choices=list_UF)
    cnpj            = models.CharField('CNPJ', max_length=11)
    consumidorFinal = models.BooleanField('Consumidor Final', default=False)
    criado          = models.DateTimeField('Criado em', auto_now_add=True)
