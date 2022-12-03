from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from MiApp.models import Avatar



class CrearJugadorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=40)

class CrearEntrenadorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    entrenado = forms.CharField(max_length=40)
    email = forms.EmailField()

class CrearTorneosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    puntos_otorgados = forms.IntegerField()

class CrearBlogsForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=400)
    #fecha_imagen = forms.DateField()
    imagen = forms.ImageField()
    


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts  = {k: '' for k in fields}





