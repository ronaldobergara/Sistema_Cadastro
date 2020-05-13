from django.urls import path
from cadastro.cad_clientes.views import novo, detail

app_name = 'cad_clientes'

urlpatterns = [
    path('', novo, name='novo'),
    path('<int:pk>/', detail, name='detail'),
]