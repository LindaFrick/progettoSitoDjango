from django.shortcuts import render
from .forms import FormRegistrazione, FormRegCliente


def registrati(request):  # pagina "registrati"

    # form BASATO sul modello cliente attraverso django
    form_reg_cliente = FormRegCliente(request.POST or None)

    if form_reg_cliente.is_valid():
        form_reg_cliente.save() #salvo i dati, non serve specificarli
        form_reg_cliente = FormRegCliente()
    return render(request, "registrati.html", {"form_cliente": form_reg_cliente})

def login(request):  # pagina "login"

    # form BASATO sul modello cliente attraverso django
    form_reg_cliente = FormRegCliente(request.POST or None)

    if form_reg_cliente.is_valid():
        form_reg_cliente.save() #salvo i dati, non serve specificarli
        form_reg_cliente = FormRegCliente()
    return render(request, "registrati.html", {"form_cliente": form_reg_cliente})
