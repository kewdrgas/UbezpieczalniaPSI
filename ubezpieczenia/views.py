from django.shortcuts import render, get_object_or_404, redirect
from .models import Ubezpieczenie
from .forms import UbezpieczenieForm, OcenaForm #, MySignupForm
from django.contrib.auth.decorators import login_required

def test_response(request):
    wszystkie = Ubezpieczenie.objects.all()
    return HttpResponse("To jest nasz pierwszy test")

#def register(request):

     #   if request.method == 'POST':
       #     form = MySignupForm(request.POST)
       #     if form.is_valid():
        #        user = form.save()

       # form = MySignupForm()
      #  return render(request, 'registration/rejestracja.html', {'form': form} )

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





