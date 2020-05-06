from django.urls import path
from cadastro.cad_clientes.views import novo

app_name = 'cad_clientes'

urlpatterns = [
    path('', novo, name='novo'),
]