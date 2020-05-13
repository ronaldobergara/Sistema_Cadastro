from django.shortcuts import render, resolve_url as r
from django.http import HttpResponseRedirect, Http404
from cadastro.cad_clientes.forms import CadClienteForm
from cadastro.cad_clientes.models import CadCliente

# Create your views here.
def novo(request):
    if request.method == 'POST':
        return inclusao(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'cad_clientes/cad_clientes_form.html',
                    {'form': CadClienteForm()})


def inclusao(request):
    form = CadClienteForm(request.POST)

    if not form.is_valid():
        return render(request, 'cad_clientes/cad_clientes_form.html',
                        {'form': form})

    cadcliente = CadCliente.objects.create(**form.cleaned_data)

    return HttpResponseRedirect(r('cad_clientes:detail', cadcliente.pk))

def detail(request, pk):
    try:
        cadcliente = CadCliente.objects.get(pk=pk)  

    except CadCliente.DoesNotExist:
        pass

    return render(request, 'cad_clientes/cad_clientes_detail.html',
                  {'cad_cliente': cadcliente})
   