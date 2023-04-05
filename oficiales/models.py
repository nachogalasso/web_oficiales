from unicodedata import category
from django.db import models

# Create your models here.
class Oficiales(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name