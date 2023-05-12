from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# from oficiales.models import NewRecruits
from .models import Availability, NewRecruits, Oficiales, Reviews

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        

class NewRecruitsForm(ModelForm):
    class Meta:
        model = NewRecruits
        fields = '__all__'
        

class AvailableOfficialsForm(ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'
        exclude = ['user']
       

class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
        

class OffialSettingsForm(ModelForm):
    class Meta:
        model = Oficiales
        fields = '__all__'
        exclude = ['user']
        


class PositionsForm(forms.Form):
    oficial = forms.ChoiceField(choices=[])
    
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super().__init__(*args, **kwargs)
        self.fields['oficial'].choices = choices
        
    