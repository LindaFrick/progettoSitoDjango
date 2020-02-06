from django.urls import path
from . import views

urlpatterns = [
    path("", views.prodotti),
    path("carrello/", views.carrello)
]