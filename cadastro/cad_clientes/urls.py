from django.urls import path
from cadastro.cad_clientes.views import novo, detail, ListaClientes

app_name = 'cad_clientes'

urlpatterns = [
    path('', novo, name='novo'),
    path('ListaClientes', ListaClientes, name='ListaClientes'),
    path('<int:pk>/', detail, name='detail'),
]