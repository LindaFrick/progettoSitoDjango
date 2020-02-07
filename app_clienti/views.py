from django.shortcuts import render, redirect
from .forms import FormRegistration, FormLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def registrati(request):  # pagina "registrati"
    form_reg = FormRegistration(request.POST or None) #dichiaro un form e metto i dati in ingresso (request.POST)

    if form_reg.is_valid(): #se il form contiene dati validi
        form_reg.save() #salvo i dati automaticamente in un oggetto User
        return redirect("/")

    context = {
        "form_cliente": form_reg #passo il form al template così lo costruisce più in fretta
    }
    return render(request, "registrati.html", context)


def login(request):  # pagina "login"

    form_login = AuthenticationForm(request.POST or None)

    if form_login.is_valid():
        #form_login.cleaned_data() #devo prendere dati e far query
        form_login = AuthenticationForm()
    return render(request, "registrati.html", {"form_login": form_login})
