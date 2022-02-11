from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Ocena, Ubezpieczenie

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['recenzja', 'gwiazdki', 'ubezpieczenie']

class UbezpieczenieForm(ModelForm):
    class Meta:
       model = Ubezpieczenie
       fields = ['tytul', 'opis', 'premiera', 'data_zakonczenia', 'znizka', 'kategoria', 'plakat', 'dodatkowe']


#class MySignupForm(UserCreationForm):
    #email = forms.EmailField(required=True)

   # class Meta:
    #        model = User
    #        fields = ('email', 'password1', 'password2')

   # def save(self, commit=True):
    #    user = super(MySignupForm, self).save(commit=False)
    #    user.email = self.cleanned_data['email']
    #    user.username = self.cleanned_data['email']

     #   if commit:
    #        user.save()
     #   return user





