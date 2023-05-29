import calendar
from unicodedata import category
from django.db import models
from .constants import *
from django.contrib.auth.models import User

# Create your models here.

# OFICIALES FAARG
class Oficiales(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    profile_pic = models.ImageField(default="user_logo_nbg.png", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# EQUIPOS
class Teams(models.Model):
    name = models.CharField(max_length=100, null=True, choices=EQUIPOS)
    logo = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# HORARIO
class Time(models.Model):
    turno = models.CharField(max_length=50, null=True, choices=HORARIO)
    
    def __str__(self):
        return self.turno

# CALENDARIO
class Calendar(models.Model):
    day = models.DateField(null=True)
    horario = models.ForeignKey(Time, null=True, on_delete=models.CASCADE)
    local = models.ForeignKey(Teams, max_length=100, null=True, on_delete=models.CASCADE, related_name='local')
    visitante = models.ForeignKey(Teams, max_length=100, null=True, on_delete=models.CASCADE, related_name='visitante')
    
    def __str__(self):
        return f"{self.day}"
    
# DISPONIBILIDAD 
class Availability(models.Model):
    
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    oficial = models.ForeignKey(Oficiales, null=True, on_delete=models.SET_NULL)
    game_date = models.ForeignKey(Calendar, null=True, on_delete=models.SET_NULL)
    partido1 = models.CharField(max_length=100, null=True, choices=STATUS, default='Si' )
    partido2 = models.CharField(max_length=100, null=True, choices=STATUS, default='Si')
    date_informed = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.oficial)

# DESIGNACIONES
class Assignment(models.Model):
    official = models.ForeignKey(Oficiales, null=True, on_delete=models.SET_NULL)
    game = models.ForeignKey(Calendar, null=True, on_delete=models.SET_NULL)
    position = models.CharField(max_length=50, null=True, choices=POSITION)
    
# REVISIONES
class Reviews(models.Model):
    
    match_date = models.CharField(max_length=100, null=True)
    play_numb = models.IntegerField(null=True)
    tiempo = models.CharField(max_length=10, null=True)
    penalty_code = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, choices=CALIFICACION)
    official_position = models.CharField(max_length=50, null=True, choices=POSITION)
    official_name = models.ForeignKey(Oficiales, max_length=100, null=True, blank=True, on_delete=models.SET_NULL)
    player_number = models.IntegerField(null=True, blank=True)
    team = models.CharField(max_length=100, null=True, choices=EQUIPOS)
    comments = models.TextField()
    
    
# INSCRIPCIONES AL CURSO DE ARBITRAJE
class NewRecruits(models.Model):
    SOCIALMEDIA = (
        ('Web FAA', 'Web FAA'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
        ('Otro', 'Otro'),
    )
    GAME = (
        ('Ninguno', 'Ninguno'),
        ('Básico', 'Básico'),
        ('Regular', 'Regular'),
        ('Bueno', 'Bueno'),
        ('Muy Bueno', 'Muy Bueno'),
        ('Excelente', 'Excelente'),
    )
    RULES_KNOWLEDGE = (
        ('Ninguno', 'Ninguno'),
        ('Básico', 'Básico'),
        ('Regular', 'Regular'),
        ('Bueno', 'Bueno'),
        ('Muy Bueno', 'Muy Bueno'),
        ('Excelente', 'Excelente'),
    )
    name = models.CharField(max_length=150, null=True)
    surname = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    age = models.IntegerField(null=True)
    socialmedia = models.CharField(max_length=150, null=True, choices=SOCIALMEDIA)
    rules = models.CharField(max_length=150, null=True)
    game = models.CharField(max_length=150, null=True, choices=GAME)
    rules_knowledge = models.CharField(max_length=150, null=True, choices=RULES_KNOWLEDGE)
    message = models.CharField(max_length=400, null=True, blank=True)
    date_inscription = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return '{} {}'.format(self.surname, self.name) 
    
