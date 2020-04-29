from django.shortcuts import render

# Create your views here.
def novo(request):
    return render(request, 'cad_clientes/cad_clientes_form.html')