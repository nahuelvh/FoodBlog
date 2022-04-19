from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField(label='E-mail:')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2' ]
        help_text = { k: "" for k in fields }


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label='Nuevo E-mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2' ]
        help_text = { k: "" for k in fields }