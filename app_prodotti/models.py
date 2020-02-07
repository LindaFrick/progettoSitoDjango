from django.db import models
from django.conf import settings


# questi modelli rappresentano le tabelle relative all'app_prodotti
class Prodotto(models.Model):
    nome = models.CharField(max_length=255)
    prezzo = models.FloatField()
    magazzino = models.IntegerField()
    immagine = models.CharField(max_length=2083) #questo attributo contiene l'url dell'immagine


class Offerta(models.Model):
    codice = models.CharField(max_length=6)
    descrizione = models.CharField(max_length=255)
    sconto = models.FloatField()


User = settings.AUTH_USER_MODEL #modello di un utente django


class CarrelloUtente(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.DO_NOTHING) #default user è admin (numero 1)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.DO_NOTHING)
