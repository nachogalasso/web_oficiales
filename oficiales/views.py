from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from .decorators import unauthenticated_user, allowed_users, admin_only

from .models import *

from .forms import  *
from django.forms import inlineformset_factory



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
# Aqui van las functions que permiten navegar por los distintos templates
def home(request):
   
    return render(request, 'oficiales/of_main.html');

def landing_page(request):
    return render(request, 'oficiales/of_incrispcion.html');

# @unauthenticated_user
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
# @login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users'])
# def ofPage(request):
#     available = request.user.oficiales.availability_set.all()
#     print('disponible: ', available)
    
#     context = {'available':available}
#     return render(request, 'oficiales/of_oficiales.html', context)


# @unauthenticated_user
# @login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users'])
def officialsPage(request, pk):
    # request_id = request.user.oficiales.id
    # oficial = Oficiales.objects.get(pk_test=request_id)
    oficial = Oficiales.objects.get(id=pk)
    games = oficial.availability_set.all()
    calendar = Calendar.objects.filter(day='2023-05-20')
    
    # Ahora creamos el contador para saber los que tenemos
    count_partido1_si = games.filter(partido1='Si').count()
    count_partido2_si = games.filter(partido2='Si').count()
    count_partido1_no = games.filter(partido1='No').count()
    count_partido2_no = games.filter(partido2='No').count()
    total_si = count_partido1_si + count_partido2_si
    total_no = count_partido1_no + count_partido2_no
    
    # 'games': games, 'total_si': total_si, 'total_no': total_no
    context = {'oficial': oficial, 'games': games, 'total_si': total_si, 'total_no': total_no, 'calendar': calendar}
     
    return render(request, 'oficiales/of_oficiales.html', context)



# @login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users', 'of_admin'])
def availabilityPage(request, pk):
    oficial = Oficiales.objects.get(id=pk)
    form = AvailableOfficialsForm(initial={'oficial': oficial})
    if request.method == 'POST':
        form = AvailableOfficialsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('officials', oficial.id)
            
    # context = {'form': form, 'available': available}
    context = {'form': form}
    return render(request, 'oficiales/of_disponibilidad.html', context);


def updateAvailability(request, pk):
    
    # oficial = Oficiales.objects.get(id=pk)
    
    available = Availability.objects.get(id=pk)
    form = AvailableOfficialsForm(instance=available)
    
    if request.method == 'POST':
        form = AvailableOfficialsForm(request.POST, instance=available)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        # else:
        #     print(form.errors)
            
    
    context = {'form': form}
    return render(request, 'oficiales/of_disponibilidad.html', context);


def deleteAvailability(request, pk):
    
    available = Availability.objects.get(id=pk)
    
    if request.method == 'POST':
        available.delete()
        return redirect('dashboard')
    
    
    context = {'available': available}
    return render(request, 'oficiales/delete.html', context)   
    
    
def inscriptionPage(request):
    return render(request, 'oficiales/of_inscripcion.html');

def inscFormPage(request):
    return render(request, 'oficiales/of_insc_form.html');

# @admin_only
def newRecruits(request):
    newRecruits = NewRecruits.objects.all()
    return render(request, 'oficiales/of_newrecruits.html', {'newRecruits': newRecruits})

# @admin_only
def dashboardPage(request):
     # Esta es la web que hace de dashboard para saber los inscriptos y los oficiales disponibles, traemos los modelos de
     # reclutas y oficiales disponibles
    newRecruits = NewRecruits.objects.all()
    oficials = Oficiales.objects.all()
    availability = Availability.objects.all()
    calendar = Calendar.objects.all()
    print(calendar)
    # Ahora creamos el contador para saber los que tenemos
    total_newRecruits = newRecruits.count()
    available1 = availability.filter(partido1='Si').count()
    available2 = availability.filter(partido2='Si').count()
    not_available1 = availability.filter(partido1='No').count()
    not_available2 = availability.filter(partido2='No').count()
    
    # Recordar que el context lo utilizamos para colocar todos los models y datos que estamos referenciando
    context = {'newRecruits': newRecruits, 'oficials': oficials, 'total_newRecruits': total_newRecruits, 'available1': available1, 'available2': available2, 'not_available1': not_available1, 'not_available2': not_available2, 'availability': availability, 'calendar': calendar}
    return render(request, 'oficiales/of_dashboard.html', context)


# CALENDAR PAGE
def calendarPage(request):
    games = Calendar.objects.all()
    logos = Teams.objects.all()
    
    # logos = games.teams_set.all()
    
    context = {'games': games, 'logos': logos}
    return render(request, 'oficiales/calendar.html',  context)


# DESIGNATIONS PAGE
# @admin_only
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

