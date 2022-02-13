from django.shortcuts import render, get_object_or_404, redirect

from .models import Ubezpieczenie, Zamowienia, Ocena
from .forms import UbezpieczenieForm, OcenaForm, ZamowieniaForm, MySignupForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

def test_response(request):
    wszystkie = Ubezpieczenie.objects.all()
    return HttpResponse("To jest nasz pierwszy test")

def register(response):

        if response.method == 'POST':
            form = MySignupForm(response.POST)
            if form.is_valid():
                user = form.save()
                return redirect("/login")
        else:
            form = MySignupForm()

        return render(response, 'registration/rejestracja.html', {'form': form})

#@login_required
#def profile(request, username):
  #     form = UserUpdateForm(request.POST, instance=request.user)

    #    if form.is_valid():
      #      user = form.save()
      #      messages.success(request, 'Twój profil został zaktualizowany!')
       #     return redirect('profile.html')

def wszystkie_ubezpieczenia(request):
    wszystkie = Ubezpieczenie.objects.all()
    return render(request, 'ubezpieczenia.html', {'ubezpieczenie': wszystkie})

def login(request):
    return render(request, 'registration/login.html')

def index(request, type='none'):
    if type=='none':
        wszystkie = Ubezpieczenie.objects.all()
    else:
        wszystkie = Ubezpieczenie.objects.kategoria()

    return render(request, 'index.html', {'ubezpieczenie': wszystkie})

def ocena_ubezpieczenia(request):
    form = OcenaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()


    return render(request, 'ocena.html', {'form': form})

@login_required
def ubezpieczenie(request, id):
    ubezpieczenie = get_object_or_404(Ubezpieczenie, pk=id)
    wszystkieOpinie= Ocena.objects.all().filter(ubezpieczenie=ubezpieczenie.id)
    user = request.user
    if request.method == "POST":
        data = request.POST
        if data.get("contact"):
            zamowienie = Zamowienia(imie=data.get("first_name"),nazwisko=data.get("last_name"),dodadkowy_opis=data.get("description"),dane_kontaktowe=data.get("contact"))
            zamowienie.save()
            zamowienie.ubezpieczenie.add(data.get("ubezpieczenie"))
            zamowienie.uzytkownik.add(user)
            zamowienie.save()
            wszystkie = Ubezpieczenie.objects.all()
            return render(request, 'index.html', {'ubezpieczenie': wszystkie ,'wszystkieOpinie':wszystkieOpinie,'tresc_wiadomosci': "Twoje zamówienie zostało dodane! Wkrótce się z Tobą skontaktujemy ;)"}) 
        else:
            ocena = Ocena(recenzja=data.get("recenzja"),gwiazdki=data.get("gwiazdki"),ubezpieczenie_id=data.get("ubezpieczenie"))
            ocena.save()
            wszystkie = Ubezpieczenie.objects.all()
            return render(request, 'index.html', {'ubezpieczenie': wszystkie ,'wszystkieOpinie':wszystkieOpinie,'tresc_wiadomosci': "Dziękujemy za dodanie opinii ;)"}) 

    return render(request,'ubezpieczenie.html', {'ubezpieczenie': ubezpieczenie,'wszystkieOpinie':wszystkieOpinie})

@login_required
def nowe_ubezpieczenie(request):
    ubezpieczenie = (Ubezpieczenie)
    form = UbezpieczenieForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        return redirect(index)

    return render(request, 'ubezpieczenie_form.html', {'form': form})


@login_required
def edytuj_ubezpieczenie(request, id):
    ubezpieczenie = get_object_or_404(Ubezpieczenie, pk=id)
    form = UbezpieczenieForm(request.POST or None, request.FILES or None, instance=ubezpieczenie)

    if form.is_valid():
        form.save()

        return redirect(index)

    return render(request, 'ubezpieczenie_form.html', {'form': form})


@login_required
def usun_ubezpieczenie(request, id):

    ubezpieczenie = get_object_or_404(Ubezpieczenie, pk=id)

    if request.method == "POST":
        ubezpieczenie.delete()
        return redirect(index)

    return render(request, 'potwierdzenie.html', {'ubezpieczenie': ubezpieczenie})


def zlozenie_zamowienia(request):
    form = ZamowieniaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, 'zamowienie.html', {'form': form})