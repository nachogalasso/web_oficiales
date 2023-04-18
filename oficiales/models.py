from unicodedata import category
from django.db import models
from .constants import *

# Create your models here.

# OFICIALES FAARG
class Oficiales(models.Model):
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.name
    

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
    

# CALENDARIO
class Calendar(models.Model):
    # HORARIO = (
    #     ('1er partido - 13hs', '1er partido - 13hs'),
    #     ('2do partido - 15.30hs', '2do partido - 15.30hs'),
    # )
    # EQUIPOS = (
    #     ('Corsarios', 'Corsarios'),
    #     ('Cruzados', 'Cruzados'),
    #     ('Jabalies', 'Jabalies'),
    #     ('Legionarios', 'Legionarios'),
    #     ('Osos Polares', 'Osos Polares'),
    #     ('Tiburones', 'Tiburones'),
    # )
    fecha = models.DateField()
    horario = models.CharField(max_length=100, null=True, choices=HORARIO)
    local = models.CharField(max_length=100, null=True, choices=EQUIPOS)
    visitante = models.CharField(max_length=100, null=True, choices=EQUIPOS)
    
    def __str__(self):
        return '{} {}'.format(self.fecha, self.horario)

    
# DISPONIBILIDAD 
class Availability(models.Model):
    # STATUS = (
    #     ('Si', 'Si'),
    #     ('No', 'No'),
    # )
    name = models.ForeignKey(Oficiales, null=True, on_delete=models.SET_NULL)
    game2 = models.ForeignKey(Calendar, null=True, on_delete=models.SET_NULL)
    partido1 = models.CharField(max_length=100, null=True, choices=STATUS, default='Si' )
    # game1 =
    partido2 = models.CharField(max_length=100, null=True, choices=STATUS, default='Si')
    date_informed = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
    
# REVISIONES
class Reviews(models.Model):
    # OFICIAL = [
    #     ('R', 'R'),
    #     ('U', 'U'),
    #     ('HL', 'HL'),
    #     ('LJ', 'LJ'),
    #     ('SJ', 'SJ'),
    #     ('FJ', 'FJ'),
    #     ('BJ', 'BJ'),
    # ]
    # STATUS = [
    #     ('Super Mal', 'Super Mal'),
    #     ('Mal', 'Mal'),
    #     ('Bien', 'Bien'),
    #     ('Muy Bien', 'Muy Bien'),
    #     ('Excelente', 'Excelente'),
    #     ('?', '?'),
    # ]
    
    match_date = models.CharField(max_length=100, null=True)
    play_numb = models.IntegerField()
    # time =
    penalty_code = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, choices=CALIFICACION)
    official = models.CharField(max_length=50, null=True, choices=OFICIAL)
    official_name = models.CharField(max_length=100, null=True)
    # player_number = models
    team = models.CharField(max_length=100, null=True, choices=EQUIPOS)
    comments = models.TextField()