from gc import disable
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

import oficiales

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


def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # user_id = request.user.id
            # oficial = Oficiales.objects.get()
            
            return redirect('officials')
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
@login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users'])
def officialsPage(request):
    oficial = Oficiales.objects.get(user=request.user)
    games = oficial.availability_set.all()
    calendar = Calendar.objects.filter(day='2023-05-20')
    time = Time.objects.all()
    
    
    # Ahora creamos el contador para saber los que tenemos
    count_partido1_si = games.filter(partido1='Si').count()
    count_partido2_si = games.filter(partido2='Si').count()
    count_partido1_no = games.filter(partido1='No').count()
    count_partido2_no = games.filter(partido2='No').count()
    total_si = count_partido1_si + count_partido2_si
    total_no = count_partido1_no + count_partido2_no
    
    # 'games': games, 'total_si': total_si, 'total_no': total_no
    context = {'oficial': oficial, 'games': games, 'total_si': total_si, 'total_no': total_no, 'calendar': calendar, 'time': time}
     
    return render(request, 'oficiales/of_oficiales.html', context)


@login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users'])
def accountSettings(request):
    oficial = request.user.oficiales 
    form = OffialSettingsForm(instance=oficial)
    
    if request.method == 'POST':
        form = OffialSettingsForm(request.POST, request.FILES,  instance=oficial)
        if form.is_valid():
            form.save()
        
    
    context = {'form': form}
    return render(request, 'oficiales/of_profile.html', context)

# @login_required(login_url='loginPage')
# @allowed_users(allowed_roles=['of_users', 'of_admin'])
# def availabilityPage(request, user_id):
    # oficial = Oficiales.objects.get(user_id=user_id)
    # form = AvailableOfficialsForm(instance=oficial)
    # if request.method == 'POST':
    #     print('request: ', request.POST)
    #     form = AvailableOfficialsForm(request.POST, instance=oficial)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('officials', oficial.user_id)
    #     else:
    #         form = AvailableOfficialsForm()
    #         print(form.errors)
def availabilityPage(request, pk):
   
    oficial = Oficiales.objects.get(id=pk)
    
    form = AvailableOfficialsForm(initial={'oficial': oficial})
    
    if request.method == 'POST':
        form = AvailableOfficialsForm(request.POST, instance=oficial)
        if form.is_valid():
            form.save()
            print(form.errors)
            return redirect('officials')
        else:
            form = AvailableOfficialsForm()
            
    context = {'form': form}
    return render(request, 'oficiales/of_disponibilidad.html', context)
    
            
    # error: 'Disponibilidad no ingresada'
    # if request.method == 'GET':
    #     return render(request, 'oficiales/of_disponibilidad.html', context)
    # else:
    #     try:
    #         form = AvailableOfficialsForm(request.POST, instance=oficial)
    #         if form.is_valid():
    #             new_available = form.save()
    #             new_available.user = request.user
    #         return redirect('officials');
    #     except ValueError:
    #         print(form.errors)
    #         return redirect('officials');
        
        
            


def updateAvailability(request, pk):
    
    available = Availability.objects.get(id=pk)
    form = AvailableOfficialsForm(instance=available)
    
    context = {'form': form}
    if request.method == 'GET':
        return render(request, 'oficiales/of_disponibilidad.html', context)
    else:
        form = AvailableOfficialsForm(request.POST, instance=available)
        if form.is_valid():
            new_available = form.save()
            new_available.user = request.user
        return redirect('officials');
    # oficial = Oficiales.objects.get(id=id)
    
    # available = Availability.objects.get()
    # form = AvailableOfficialsForm(instance=available)
    
    # if request.method == 'POST':
    #     form = AvailableOfficialsForm(request.POST, instance=available)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('officials')
        # else:
        #     print(form.errors)
            
    
    # return render(request, 'oficiales/of_disponibilidad.html', context);


def deleteAvailability(request, pk):
    
    available = Availability.objects.get(id=pk)
    print(available)
    
    if request.method == 'POST':
        available.delete()
        return redirect('officials')
    
    
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
    time = Time.objects.all()
    
    # Ahora creamos el contador para saber los que tenemos
    total_newRecruits = newRecruits.count()
    available1 = availability.filter(partido1='Si').count()
    available2 = availability.filter(partido2='Si').count()
    not_available1 = availability.filter(partido1='No').count()
    not_available2 = availability.filter(partido2='No').count()
    
    # Recordar que el context lo utilizamos para colocar todos los models y datos que estamos referenciando
    context = {'newRecruits': newRecruits, 'oficials': oficials, 'total_newRecruits': total_newRecruits, 'available1': available1, 'available2': available2, 'not_available1': not_available1, 'not_available2': not_available2, 'availability': availability, 'calendar': calendar, 'time': time}
    return render(request, 'oficiales/of_dashboard.html', context)


# CALENDAR PAGE
def calendarPage(request):
    games = Calendar.objects.all()
    logos = Teams.objects.all()
   
    context = {'games': games, 'logos': logos}
    return render(request, 'oficiales/calendar.html',  context)


# DESIGNATIONS PAGE
# @admin_only
def designationsPage(request):
    oficiales = Availability.objects.all()
    game1 = Availability.objects.filter(partido1='Si')
    game2 = Availability.objects.filter(partido2='Si')
    
    official_choices = [("", "---------")] + [(availability.oficial.id, str(availability.oficial)) for availability in game1]
    form = PositionsForm(choices=official_choices, initial={'oficial': ''})
    official_choices2 = [("", "---------")] + [(availability.oficial.id, str(availability.oficial)) for availability in game2]
    form2 = PositionsForm(choices=official_choices2, initial={'oficial': ''})
    
    
    context = {'oficiales':oficiales, 'game1': game1, 'game2': game2, 'form': form, 'form2': form2}
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

