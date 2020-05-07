from django.contrib import admin

from .models import Vuelo, Aereopuerto,Pasajero

admin.site.register(Vuelo)
admin.site.register(Aereopuerto)
admin.site.register(Pasajero)

# Register your models here.
