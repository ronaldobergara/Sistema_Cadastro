from django.shortcuts import render, resolve_url as r, get_object_or_404
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

    cadcliente = form.save()

    return HttpResponseRedirect(r('cad_clientes:detail', cadcliente.pk))

def detail(request, pk):
    try:
        cadcliente = CadCliente.objects.get(pk=pk)  

    except CadCliente.DoesNotExist:
        pass

    return render(request, 'cad_clientes/cad_clientes_detail.html',
                  {'cad_cliente': cadcliente})
   

def ListaClientes(request):

    lista_clientes = CadCliente.objects.all()

    return render(request, 'cad_clientes/lista_clientes.html',
                  {'lista_clientes': lista_clientes})

def Alteracao(request, pk):
    cliente = CadCliente.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CadClienteForm(request.POST, instance=cliente)

        if not form.is_valid():
            return render(request, 'cad_clientes/cad_clientes_form.html',
                {'form': form})

        form.save()
        return HttpResponseRedirect(r('cad_clientes:ListaClientes'))
    else:
        form = CadClienteForm(instance=cliente)   
        return render(request, 'cad_clientes/cad_clientes_form.html', {'form': form})

def Exclusao(request, pk):
    cliente = CadCliente.objects.get(pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        return HttpResponseRedirect(r('cad_clientes:ListaClientes'))


    # form = CadClienteForm(instance=cliente)   
    return render(request, 'cad_clientes/cad_cliente_confirma_exclusao.html', {'cliente': cliente})    



             
