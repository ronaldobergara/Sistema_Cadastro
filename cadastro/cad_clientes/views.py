from django.shortcuts import render
from cadastro.cad_clientes.forms import CadClienteForm

# Create your views here.
def novo(request):
    if request.method == 'POST':
        pass

    return empty_form(request)


def empty_form(request):
    return render(request, 'cad_clientes/cad_clientes_form.html',
                    {'form': CadClienteForm()})


def inclusao(request):
    form = CadClienteForm(request.POST)

    

