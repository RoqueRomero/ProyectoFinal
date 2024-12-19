from django.shortcuts import get_object_or_404,render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from Usuarios.forms import UserRegisterForm

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
           #return render(request,"productos/index.html")
        msg_registro="Datos incorrectos"
    form=UserRegisterForm()
    return render(request,"Usuarios/registro.html",{"form":form,"msg_registro":msg_registro})    
    



def usuario_perfil():
    pass
            
            
        
        
