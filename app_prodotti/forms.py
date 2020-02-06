from django import forms
from .models import CarrelloUtente


class FormAggiungiCarrello(forms.ModelForm):  # form BASATO sul modello carrello (tutto basato su django)
    class Meta:
        model = CarrelloUtente
        fields = ['cliente', 'prodotto']

