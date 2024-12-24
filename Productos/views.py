
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from Productos.models import Item
from .forms import CrearProducto

# Create your views here.

def inicio(request):
    return render(request,"Productos/iniciop.html")



#listar
class listar(ListView):
    model=Item
    template_name="Productos/listar.html"
    
        
    def envio(self,request):
        valores=Item.objects.all()
        return render(request,self.template_name,{'items':valores})
    



class detalle(DetailView):
    model=Item
    template_name="Productos/detalle.html"
    
    
    def busca(request,pk):
        variable=get_object_or_404(Item,pk=pk) 
        if request.method=='GET':
            return render(request,"Productos/detalle.html",{'item':variable})
    

#crear
class crear(CreateView):
    model= Item
    form_class = CrearProducto
    template_name="Productos/crear.html"
    # fields=["nombre","marca","descripcion"]
    success_url=reverse_lazy('listar')
    


#editar
class editar():
    pass

#borrar
class borrar():
    pass

