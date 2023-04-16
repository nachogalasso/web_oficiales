from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# from oficiales.models import NewRecruits
from .models import Availability, NewRecruits, Oficiales, Reviews

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class NewRecruitsForm(ModelForm):
    class Meta:
        model = NewRecruits
        fields = '__all__'
        

class AvailableOfficialsForm(ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'