from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from ubezpieczenia.views import test_response, wszystkie_ubezpieczenia, login, index, ocena_ubezpieczenia, nowe_ubezpieczenie, edytuj_ubezpieczenie, usun_ubezpieczenie#, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response),
    path('login/', auth_views.LoginView.as_view(), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout"),
    #path('register/', view.register, name = "register"),
    path('index/', index, name="index"),
    path('ocena/', ocena_ubezpieczenia, name="ocena_ubezpieczenia"),
    path('wszystkie_ubezpieczenia/', wszystkie_ubezpieczenia, name="wszystkie_ubezpieczenia"),
    path('nowe_ubezpieczenie/', nowe_ubezpieczenie, name="nowe_ubezpieczenie"),
    path('edytuj_ubezpieczenie/<int:id>/', edytuj_ubezpieczenie, name="edytuj_ubezpieczenie"),
    path('usun_ubezpieczenie/<int:id>/', usun_ubezpieczenie, name="usun_ubezpieczenie")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

