from django import forms
from django.utils.safestring import mark_safe

from .models import Cliente


class FormRegistrazione(forms.Form):  # form con gli stessi campi del modello "cliente"
    nome = forms.CharField(max_length=255)
    cognome = forms.CharField(max_length=255)
    mail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class FormRegCliente(forms.ModelForm):  # form BASATO sul modello cliente (tutto basato su django)
    class Meta:
        model = Cliente
        fields = ['nome', 'cognome', 'mail', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_mail(self, *args, **kwargs):  # funzione per stampare errori personalizzati sulla validazione dell'email
        mail = self.cleaned_data.get('mail')
        query = Cliente.objects.filter(
            mail__iexact=mail)  # prendo clienti da db con questa mail (anche se ha lettere maiuscole o minuscole diverse --> ixact)

        if not (mail.endswith(".com")) and not (mail.endswith(".it")):
            raise forms.ValidationError("Questa non è una mail valida. Inserire '.com' o .'it'")
        elif query.exists():
            raise forms.ValidationError("Questa mail esiste già")
        return mail
