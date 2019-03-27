from django.urls import path
from . import views#agregamos toda snuestras vistas

urlpatterns = [
    path('', views.post_list, name='post_list'),#detectara la cadena vacia, y el URL resolver de Django no tiene en cuenta el nombre el dominio
]


