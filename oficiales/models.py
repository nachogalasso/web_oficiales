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
    name = models.CharField(max_length=150, null=True)
    surname = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)
    age = models.IntegerField(null=True)