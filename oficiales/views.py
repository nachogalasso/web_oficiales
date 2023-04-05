from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Aqui van las functions que permiten navegar por los distintos templates
def home(request):
    return render(request, 'oficiales/of_main.html');

def landing_page(request):
    return render(request, 'oficiales/of_incrispcion.html');


def loginPage(request):
    return render(request, 'oficiales/login.html');

def availabilityPage(request):
    return render(request, 'oficiales/availability.html');

def inscriptionPage(request):
    return render(request, 'oficiales/of_inscripcion.html');

def inscFormPage(request):
    return render(request, 'oficiales/of_insc_form.html');






