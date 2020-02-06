from django.db import models


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

class CarrelloUtente(models.Model):
    cliente = models.IntegerField()
    prodotto = models.IntegerField()