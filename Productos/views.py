from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from Productos.models import Item

# Create your views here.
#listar
class listar(ListView):
    model=Item
    template_name="Productos/listar.html"

class detalle(DetailView):
    model=Item
    template_name="Productos/detalle.html"
    

#crear
class crear(CreateView):
    model=Item
    template_name="Productos/crear.html"
    fields=["nombre","marca","descripcion"]

    

#editar
class editar():
    pass

#borrar
class borrar():
    pass

#Acerca de mi
class about():
    pass


