from django.urls import path 


from Usuarios.views import usuario_login,usuario_registrar,usuario_perfil


urlpatterns = [
    path('login/',usuario_login),
    path('registrar/',usuario_registrar),
    path('perfil/',usuario_perfil)
    

    
]

