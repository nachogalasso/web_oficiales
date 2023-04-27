from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from django.template import loader

from .decorators import unauthenticated_user, allowed_users, admin_only

from .models import *

from .forms import  *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
# Aqui van las functions que permiten navegar por los distintos templates
def home(request):
   
    return render(request, 'oficiales/of_main.html');

def landing_page(request):
    return render(request, 'oficiales/of_incrispcion.html');

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'El usuario o la password no es correcto.')
            # return render(request, 'oficiales/login.html');
        
    context = {}        
    return render(request, 'oficiales/login.html', context);

def logoutUser(request):
    logout(request)
    return redirect('loginPage')

# DISPONIBILIDADES
# @unauthenticated_user
# @login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users'])
def officialsPage(request, pk):
    
    # oficials = Oficiales.objects.get(id=pk)
    oficial = Oficiales.objects.get(id=pk)
    games = oficial.availability_set.all()
    
    # Ahora creamos el contador para saber los que tenemos
    count_partido1_si = games.filter(partido1='Si').count()
    count_partido2_si = games.filter(partido2='Si').count()
    count_partido1_no = games.filter(partido1='No').count()
    count_partido2_no = games.filter(partido2='No').count()
    total_si = count_partido1_si + count_partido2_si
    total_no = count_partido1_no + count_partido2_no
    
    
    context = {'oficial': oficial, 'games': games, 'total_si': total_si, 'total_no': total_no}
     
    return render(request, 'oficiales/of_oficiales.html', context)



# @login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users', 'of_admin'])
def availabilityPage(request):
    form = AvailableOfficialsForm()
    
    if request.method == 'POST':
        # print('a ver si funciona', request.POST)
        form = AvailableOfficialsForm(request.POST)
        if form.is_valid():
            # respuesta = form.save(commit=False)
            # respuesta.oficial = request.user
            # respuesta.save()
            form.save()
            return redirect('dashboard')
        # else:
        #     form = AvailableOfficialsForm()
            
    context = {'form': form}
    return render(request, 'oficiales/of_disponibilidad.html', context);


def updateAvailability(request, pk):
    
    available = Availability.objects.get(id=pk)
    form = AvailableOfficialsForm(instance=available)
    
    if request.method == 'POST':
        form = AvailableOfficialsForm(request.POST, instance=available)
        if form.is_valid():
            form.save()
            return redirect('dashboard' )
    
    context = {'form': form}
    return render(request, 'oficiales/of_disponibilidad.html', context);
    
    
    
def inscriptionPage(request):
    return render(request, 'oficiales/of_inscripcion.html');

def inscFormPage(request):
    return render(request, 'oficiales/of_insc_form.html');

@admin_only
def newRecruits(request):
    newRecruits = NewRecruits.objects.all()
    return render(request, 'oficiales/of_newrecruits.html', {'newRecruits': newRecruits})

@admin_only
def dashboardPage(request):
     # Esta es la web que hace de dashboard para saber los inscriptos y los oficiales disponibles, traemos los modelos de
     # reclutas y oficiales disponibles
    newRecruits = NewRecruits.objects.all()
    oficials = Oficiales.objects.all()
    availability = Availability.objects.all()
    
    # Ahora creamos el contador para saber los que tenemos
    total_newRecruits = newRecruits.count()
    available = availability.filter(partido1='Si').count() + availability.filter(partido2='Si').count()
    not_available = availability.filter(partido1='No').count() + availability.filter(partido2='No').count()
    
    # Recordar que el context lo utilizamos para colocar todos los models y datos que estamos referenciando
    context = {'newRecruits': newRecruits, 'oficials': oficials, 'total_newRecruits': total_newRecruits, 'available': available, 'not_available': not_available, 'availability': availability}
    return render(request, 'oficiales/of_dashboard.html', context)


# CALENDAR PAGE
def calendarPage(request):
    games = Calendar.objects.all()
    
    context = {}
    return render(request, 'oficiales/calendar.html',  {'games': games})


# DESIGNATIONS PAGE
@admin_only
def designationsPage(request):
    oficiales = Availability.objects.all()
    respuestas = Availability.objects.filter(oficial=request.user)
    
    context = {'oficiales':oficiales, 'respuestas':respuestas}
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