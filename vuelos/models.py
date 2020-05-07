from django.db import models

class Aereopuerto(models.Model):
    codigo=models.CharField(max_length=4)
    ciudad =models.CharField(max_length=70)
    def __str__(self):
        return f"({self.codigo}) --  {self.ciudad}"
    
class Vuelo(models.Model):
    origen = models.ForeignKey(Aereopuerto,on_delete=models.CASCADE,related_name="salida") # relacion de uno a muchos
    destino = models.ForeignKey(Aereopuerto,on_delete=models.CASCADE,related_name="llegadas") # relacion de uno a muchos
    duracion = models.IntegerField(null=True)
    
    def __str__(self):
        return f"({self.id})  -- {self.origen}  hasta {self.destino}"  #para que nos traiga de forma ordenada
    

class Pasajero(models.Model):
    nombre = models.CharField(max_length=70)
    apellidos =models.CharField(max_length=70)
    vuelo=models.ManyToManyField(Vuelo,blank=True,related_name="pasajeros")
    
    def __str__(self):
        return f"{self.nombre} - {self.apellidos}"

# Create your models here.
