from django.db import models

# Create your models here.
class CadCliente(models.Model):
    razaoSocial     = models.CharField('Razão Social', max_length=150)   
    nomeFantasia    = models.CharField('Nome Fantasia', max_length=100)
    cep             = models.CharField('CEP', max_length=8)
    endereco        = models.CharField('Endereço', max_length=200)
    numero          = models.CharField('Numero', max_length=10)
    uf              = models.CharField('UF', max_length=2)
    cnpj            = models.CharField('CNPJ', max_length=11)
    consumidorFinal = models.BooleanField('Consumidor Final', default=False)
    criado          = models.DateTimeField('Criado em', auto_now_add=True)
