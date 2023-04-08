from unicodedata import category
from django.db import models

# Create your models here.
class Oficiales(models.Model):
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.name
    
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
    
    
class Availability(models.Model):
    STATUS = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    name = models.ForeignKey(Oficiales, null=True, on_delete=models.SET_NULL)
    # game =
    date_informed = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True, choices=STATUS)