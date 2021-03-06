from django.contrib import admin
from .models import Ubezpieczenie
from .models import Ubezpieczenie, Ocena, Obiekt_ubezpieczony, Zamowienia
#admin.site.register(Ubezpieczenie)

@admin.register(Ubezpieczenie)
class UbezpiecznieAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "znizka", "premiera", "data_zakonczenia", "kategoria"]
    list_filter = ("znizka", "premiera", "data_zakonczenia", "kategoria")
    search_fields = ("tytul", "opis")

admin.site.register(Obiekt_ubezpieczony)
admin.site.register(Ocena)
admin.site.register(Zamowienia)