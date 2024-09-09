from django import forms
from .models import MovieModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = ['id','name','description','image','user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder':'description'}),
            'image': forms.FileInput(attrs={'class': 'form-control','placeholder':'image'}),
        }
        
class registrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')