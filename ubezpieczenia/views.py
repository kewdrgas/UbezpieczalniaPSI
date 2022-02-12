from django.shortcuts import render, get_object_or_404, redirect
from .models import Ubezpieczenie
from .forms import UbezpieczenieForm, OcenaForm, ZamowieniaForm, MySignupForm#, UserUpdateForm
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

def index(request):
    wszystkie = Ubezpieczenie.objects.all()
    return render(request, 'index.html', {'ubezpieczenie': wszystkie})

def ocena_ubezpieczenia(request):
    form = OcenaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()


    return render(request, 'ocena.html', {'form': form})
def ubezpieczenie(request, id):
    ubezpieczenie = get_object_or_404(Ubezpieczenie, pk=id)
    return render(request,'ubezpieczenie.html', {'ubezpieczenie': ubezpieczenie})

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