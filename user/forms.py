
#To modify our forms to have like email session and more
from django import forms
from .models import Profile 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    #To define how we want our form to look like
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']   # Here you enter all the things you want to see on your form field
        
class UserUpdateForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['username', 'email']
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']