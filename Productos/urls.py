from django.urls import path 


import Productos
from Productos import views
from Productos.views import *


urlpatterns = [
    path('items/',listar.as_view(), name="listar"),
    path('items/<pk>',detalle.as_view(),name="detalle"),    
    path('crear/',crear.as_view(), name="crear"),
    path('listar/',listar.as_view()),
    path('inicio/',views.inicio),
    path('editar/<pk>',editar.as_view(),name="actualizar"),
    # path('borrar/',borrar),
]