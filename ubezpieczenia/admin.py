from django.contrib import admin
from .models import Ubezpieczenie
from .models import Ubezpieczenie, DodatkoweInfo, Ocena, Obiekt_ubezpieczony
#admin.site.register(Ubezpieczenie)

@admin.register(Ubezpieczenie)
class UbezpiecznieAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "znizka", "premiera", "data_zakonczenia"]
    list_filter = ("znizka", "premiera", "data_zakonczenia")
    search_fields = ("tytul", "opis")

admin.site.register(DodatkoweInfo)
admin.site.register(Obiekt_ubezpieczony)
admin.site.register(Ocena)