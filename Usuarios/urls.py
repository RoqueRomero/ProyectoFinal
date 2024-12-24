from django.urls import path 


from Usuarios.views import usuario_login,usuario_registrar,usuario_perfil,inicio
from Usuarios import views



urlpatterns = [
    path('login/',usuario_login),
    path('registrar/',usuario_registrar),
    path('perfil/',usuario_perfil),
    path('inicio/',views.inicio),
    

    
]

