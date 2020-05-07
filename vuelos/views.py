from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from django.urls import reverse


def index(request):
    context ={
        "vuelos":Vuelo.objects.all()
    }
    return render(request, "index.html", context)

def vuelo(request,vuelo_id):
    try:
        vuelo=Vuelo.objects.get(pk=vuelo_id)
    except Vuelo.DoesNotExist:
        raise Http404("vuelo no existe")
    context ={
        "vuelo":vuelo,
        "pasajeros":vuelo.pasajeros.all(),
        "no_pasajeros":Pasajero.objects.exclude(vuelo=vuelo).all()
    }
    return render(request,"vuelo.html",context)


def reservar(request,vuelo_id):
    try:
        pasajero_id=int(request.POST["pasajero"])
        pasajero=Pasajero.objects.get(pk=pasajero_id)
        vuelo=Vuelo.objects.get(pk=vuelo_id)
    except KeyError:
        return render(request,"error.html",{"msg":"No Selecciono Pasajero"})
    except Vuelo.DoesNotExist:
        return render(request,"error.html",{"msg":"No Existe el vuelo"})
    except Pasajero.DoesNotExist:
        return render(request,"error.html",{"msg":"No Existe pasajero"})
    
    pasajero.vuelo.add(vuelo)
    return HttpResponseRedirect(reverse("vuelo",args=(vuelo_id,)))

        
    


# Create your views here.
