from django.shortcuts import render
from django.http import HttpResponse
from .models import Prodotto, CarrelloUtente #importiamo la classe prodotto per accedere ai dati delle tabelle
from django.contrib.auth.decorators import login_required
from .forms import FormAggiungiCarrello


def prodotti(request):
    prodotti = Prodotto.objects.all()

    '''
    for prodotto in prodotti:

        form_aggiungi = FormAggiungiCarrello(initial={'cliente': 1, 'prodotto': prodotto})
        form_aggiungi.save()  # salvo i dati, non serve specificarli
, "form": form_aggiungi
    '''

    return render(request, "prodotti.html", {"prodotti": prodotti}) #il terzo argomento sono i dati da passare a prodotti.html


@login_required
def carrello(request):

    carrelli = CarrelloUtente.objects.all() #query per prodotti nel carrello dell'utente
    return render(request, "carrello.html", {"carrelli": carrelli})
