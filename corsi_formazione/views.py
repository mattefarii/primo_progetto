from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Corso
from datetime import datetime


def home(request):
    c = []
    

    for corso in Corso.objects.all():
        c.append (corso.titolo)

    response = str(c) 
    print(response)

    return HttpResponse("<h1>Homepage Corsi!</h1>")

# Create your views here.


def viewA (request, pk=None):
    corsi = Corso.objects.all()
    context = {
        "corsi": corsi,
    }
    return render (request, "viewA.html", context)

def viewB (request, pk=None):
    corsi = Corso.objects.all()
    context = {
        "corsi": corsi,
    }
    return render (request, "viewB.html", context)

def viewC (request, pk=None):
    corsi = Corso.objects.all()
    context = {
        "corsi": corsi,
    }
    return render (request, "viewC.html", context)

def viewD (request, pk=None):
    corsi = Corso.objects.all()
    context = {
        "corsi": corsi,
    }
    return render (request, "viewD.html", context)

def viewE (request, pk=None):
    corsi = Corso.objects.all()
    context = {
        "corsi": corsi,
    }
    return render (request, "viewE.html", context)


#corso_dopo_data = Corso.objects.filter(data=datetime.date(2025, 1, 5))

#corso_posti_20 = Corso.objects.filter(corso_posti_gte = 20).distinct()

#corso_posti_20 = Corso.objects.filter(corso_posti_gte = 20).distinct()