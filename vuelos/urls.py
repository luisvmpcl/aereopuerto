from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:vuelo_id>",views.vuelo,name="vuelo"),
    path("<int:vuelo_id>/reservar",views.reservar,name="reservar"),
    
]