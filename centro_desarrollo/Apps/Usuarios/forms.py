from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,min_length=5,label='Ingresa tu usuario',required=True,widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    password = forms.CharField(max_length=50,min_length=5,label='Ingresa tu contraseña',required=True,widget=forms.TextInput(attrs={'placeholder':'Password','class':'form-control'}))

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa el usuario que tendras'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingresa la contraseña de mininmo 8 caracteres'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'correo@correo.com'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu apellido'})
        }
        help_texts = {
            'username': 'Maximo 150 caracteres',
            'password': 'Minimo 8 caracteres'
        }