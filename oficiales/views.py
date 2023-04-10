from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

from .models import *

# Create your views here.
# Aqui van las functions que permiten navegar por los distintos templates
def home(request):
   
    return render(request, 'oficiales/of_main.html');

def landing_page(request):
    return render(request, 'oficiales/of_incrispcion.html');


def loginPage(request):
    return render(request, 'oficiales/login.html');


# DISPONIBILIDADES
def availabilityPage(request):
    
    return render(request, 'oficiales/of_disponibilidad.html');

# def disp_form4(request):
#     return render(request, 'oficiales/disp_form4.html');

def inscriptionPage(request):
    return render(request, 'oficiales/of_inscripcion.html');

def inscFormPage(request):
    return render(request, 'oficiales/of_insc_form.html');


def newRecruits(request):
    newRecruits = NewRecruits.objects.all()
    return render(request, 'oficiales/of_newrecruits.html', {'newRecruits': newRecruits})


def dashboardPage(request):
     # Esta es la web que hace de dashboard para saber los inscriptos y los oficiales disponibles
    newRecruits = NewRecruits.objects.all()
    oficials = Oficiales.objects.all()
    
    # Recordar que el context lo utilizamos para colocar todos los models y datos que estamos referenciando
    context = {'newRecruits': newRecruits, 'oficials': oficials}
    return render(request, 'oficiales/of_dashboard.html', context)





