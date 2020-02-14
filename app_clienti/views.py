from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import FormRegistration
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def registrati(request):  # pagina "registrati"
    form_reg = FormRegistration(request.POST or None) #dichiaro un form e metto i dati in ingresso (request.POST)

    if form_reg.is_valid(): #se il form contiene dati validi
        form_reg.save() #salvo i dati automaticamente in un oggetto User
        return redirect("/")

    context = {
        "form_cliente": form_reg #passo il form al template così lo costruisce più in fretta
    }
    return render(request, "registrati.html", context)


def login_page(request):  # pagina "login"
    form_login = AuthenticationForm(data=request.POST or None)

    if form_login.is_valid():

        #django authentication system
        user = authenticate( #se ha successo restituisce un oggetto User, altrimenti None
            request,
            username=form_login.cleaned_data.get('username'),
            password=form_login.cleaned_data.get('password')
        )

        if user is None:
            return render(
                request,
                'login.html',
                {'form': form_login, 'invalid_creds': True}

            )


        try:
            form_login.confirm_login_allowed(user) #per verificare che l'utente sia attivo (??)
        except ValidationError:
            return render(
                request,
                'login.html',
                {'form': form_login, 'invalid_creds': True}
            )
        login(request, user) #associo l'utente alla sessione

        return redirect("/")

    return render(request, "login.html", {"form_login": form_login, "invalid_creds": False})


@login_required
def logout_page(request):
    logout(request)
    return redirect("/")
