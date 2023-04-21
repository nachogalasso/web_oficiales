from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

from .models import *

from .forms import  *

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
    
    form = AvailableOfficialsForm()
    
    context = {'form': form}
    
    if request.method == 'POST':
        # print('a ver si funciona', request.POST)
        form = AvailableOfficialsForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'oficiales/of_disponibilidad.html', context);

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
     # Esta es la web que hace de dashboard para saber los inscriptos y los oficiales disponibles, traemos los modelos de
     # reclutas y oficiales disponibles
    newRecruits = NewRecruits.objects.all()
    oficials = Oficiales.objects.all()
    availability = Availability.objects.all()
    
    # Ahora creamos el contador para saber los que tenemos
    total_newRecruits = newRecruits.count()
    available = availability.filter(partido1='Si').count() + availability.filter(partido2='Si').count()
    not_available = availability.filter(partido2='No').count() + availability.filter(partido2='No').count()
    
    # Recordar que el context lo utilizamos para colocar todos los models y datos que estamos referenciando
    context = {'newRecruits': newRecruits, 'oficials': oficials, 'total_newRecruits': total_newRecruits, 'available': available, 'not_available': not_available}
    return render(request, 'oficiales/of_dashboard.html', context)


# CALENDAR PAGE
def calendarPage(request):
    return render(request, 'oficiales/calendar.html')


# DESIGNATIONS PAGE
def designationsPage(request):
    oficiales = Availability.objects.all()
    
    
    context = {'oficiales':oficiales}
    return render(request, 'oficiales/of_designaciones.html', context)


# REVIEWS PAGE
def reviewPage(request):
    reviewsForm = ReviewsForm()
    
    if request.method == 'POST':
        # print(request.POST) tengo que probar eso
        reviewsForm = ReviewsForm(request.POST)
        if reviewsForm.is_valid():
            reviewsForm.save()
            
    reviews = Reviews.objects.all()
    
    context = {'reviewsForm': reviewsForm, 'reviews': reviews}
    
    return render(request, 'oficiales/of_revisiones.html', context)




# EN EL VIDEO 15 DEL CURSO DE DJANGO TENGO LA EXPLICACION PARA GENERAR LOS PERMISOS DE LOS USUARIOS
# LO MEJOR VA A SER CREAR LOS GRUPOS, UNO PARA LOS OFICIALES Y OTRO PARA LOS ADMIN