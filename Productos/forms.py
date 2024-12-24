from django import forms 
from .models import Item

class CrearProducto (forms.ModelForm): 
    class  Meta : 
        model = Item
        fields = [ 'nombre' , 'marca','descripcion']

