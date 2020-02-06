from django.contrib import admin
from app_prodotti.models import Prodotto, Offerta, CarrelloUtente

# Register your models here.

admin.site.register(Prodotto)
admin.site.register(Offerta)
admin.site.register(CarrelloUtente)
