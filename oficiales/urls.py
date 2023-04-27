from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('of_inscripcion', views.landing_page, name='landingPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('available/', views.availabilityPage, name='available'),
    path('update_available/<str:pk>', views.updateAvailability, name='update_available'),
    path('designations/', views.designationsPage, name='designations'),
    path('games/<str:pk>/', views.officialsPage, name='of_games'),
    path('inscription/', views.inscriptionPage, name='inscription'),
    path('inscForm/', views.inscFormPage, name='inscForm'),
    path('newrecruits/', views.newRecruits, name='newRecruits'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('calendar/', views.calendarPage, name='calendar'),
    path('revisiones/', views.reviewPage, name='reviews'),
]
