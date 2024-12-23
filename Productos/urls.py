from django.urls import path 


from Productos.views import *


urlpatterns = [
    path('items/',listar.as_view()),
    path('items/<pk>',detalle.as_view(),name="detalle"),    
    path('crear/',crear.as_view()),
    # path('editar/',editar),
    # path('borrar/',borrar),
]