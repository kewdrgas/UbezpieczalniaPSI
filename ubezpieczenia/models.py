from django.db import models

# Create your models here.

class DodatkoweInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Samochód'),
        (2, 'Dom'),
        (3, 'Zdrowotne'),
        (4, 'Elektronika'),
    }
    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)


class Ubezpieczenie(models.Model):
    tytul = models.CharField(max_length=64, blank=False)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    data_zakonczenia = models.DateField(null=True, blank=True)
    znizka = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    kategoria = models.TextField(default="")
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)
    dodatkowe = models.OneToOneField(DodatkoweInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tytul

class Ocena(models.Model):
    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    ubezpieczenie = models.ForeignKey(Ubezpieczenie, on_delete=models.CASCADE)

class Obiekt_ubezpieczony(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    ubezpieczenie = models.ManyToManyField(Ubezpieczenie, related_name="obiekt_ubezpieczony")
