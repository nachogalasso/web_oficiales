from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('of_inscripcion', views.landing_page, name='landingPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('availability/', views.availabilityPage, name='availability'),
    path('inscription/', views.inscriptionPage, name='inscription'),
    path('inscForm/', views.inscFormPage, name='inscForm'),
    path('newrecruits/', views.newRecruits, name='newRecruits'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    # path('/', views.disp_form4, name='disp_form4'),
]
