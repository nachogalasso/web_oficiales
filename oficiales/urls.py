from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('of_inscripcion', views.landing_page, name='landingPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('officials/', views.officialsPage, name='officials'),
    path('account/', views.accountSettings, name='acc_settings'),
    path('available/<str:pk>', views.availabilityPage, name='available'),
    path('update_available/<str:pk>', views.updateAvailability, name='update_available'),
    path('delete_available/<str:pk>', views.deleteAvailability, name='delete_available'),
    path('designations/', views.designationsPage, name='designations'),
    path('inscription/', views.inscriptionPage, name='inscription'),
    path('inscForm/', views.inscFormPage, name='inscForm'),
    path('newrecruits/', views.newRecruits, name='newRecruits'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('calendar/', views.calendarPage, name='calendar'),
    path('revisiones/', views.reviewPage, name='reviews'),
] 

    # path('of_page/', views.ofPage, name='of_page'),

""" 
Para poder desplegar las imágenes en la web luego de cargarlas en el admin
 from django.conf import settings
 from django.conf.urls.static import static
 
 urlpatterns = [
     
 ] + + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
