from django.shortcuts import get_object_or_404,render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
#Esto es un decorador que sirve para que solo usuarios autenticados puedan acceder 
from django.contrib.auth.decorators import login_required

from Usuarios.forms import UserRegisterForm, UserEditForm
from Usuarios.models import Imagen

# Create your views here.
def usuario_login(request):
    msg_login = ""
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contrasenia=form.cleaned_data.get('password')
            
            user=authenticate(username=usuario,password=contrasenia)
            if user is not None:
                login(request,user)
                return render(request,'Usuarios/index.html')
            msg_login="Usuario o contraseña incorrectos"
    form=AuthenticationForm()
    return render(request,'Usuarios/login.html',{"form":form,"msg_login":msg_login})    


def usuario_registrar(request):
    msg_registro=""
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request,"Productos/index.html")
        msg_registro="Error Datos incorrectos"
    form=UserRegisterForm()
    return render(request,"Usuarios/registro.html",{"form":form,"msg_registro":msg_registro})    
    
@login_required
def usuario_perfil(request):
    usuario=request.user
    
    if request.method=='POST':
        miFormulario=UserEditForm(request.Post,request.FILES,instance=usuario)
        if miFormulario.is_valid():        
            if miFormulario.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user=usuario).exists():
                    usuario.imagen.imagen=miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()
                else:
                    avatar=Imagen(user=usuario,imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()
                    
        miFormulario.save()
        return render(request,"Productos/index.html")
    else:
        miFormulario=UserEditForm(instance=usuario)


        
        
            
        
        
