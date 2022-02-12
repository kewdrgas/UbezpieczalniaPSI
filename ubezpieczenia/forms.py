from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Ocena, Ubezpieczenie, Zamowienia

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['recenzja', 'gwiazdki', 'ubezpieczenie']

class UbezpieczenieForm(ModelForm):
    class Meta:
       model = Ubezpieczenie
       fields = ['tytul', 'opis', 'premiera', 'data_zakonczenia', 'znizka', 'kategoria', 'plakat', 'dodatkowe']

class ZamowieniaForm(ModelForm):
    class Meta:
        model = Zamowienia
        fields = ['imie', 'nazwisko', 'ubezpieczenie', 'dodadkowy_opis' , 'dane_kontaktowe']

class MySignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MySignupForm, self).save(commit=False)


        if commit:
            user.save()

#class UserUpdateForm(forms.ModelForm):
  #  email = forms.EmailField(required=True)

   # class Meta:
    #    model = User
    #    fields = ['username', 'first_name', 'last_name', 'email']






