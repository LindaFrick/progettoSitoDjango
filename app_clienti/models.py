from django.db import models


# questi modelli rappresentano le tabelle relative all'app app_clienti
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cognome = models.CharField(max_length=255)
    mail = models.CharField(max_length=255, default="gigi@gmail.com", unique=True)
    password = models.CharField(max_length=30, default="ciao")

