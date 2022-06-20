from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Publicacion_formulario(forms.Form):
    usuario = forms.CharField(max_length=40)
    tema_especifico = forms.CharField(max_length=40)
    consulta = forms.CharField(widget=forms.Textarea)
    
class Contacto_formulario(forms.Form):
    usuario = forms.CharField(max_length=40)
    email = forms.EmailField()
    razon_contacto = forms.CharField(widget=forms.Textarea)
    
class Sorteo_formulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    telefono = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir constraseña' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Nuevo nombre de usuario')
    email = forms.EmailField(label= 'Nuevo email')
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}

class Comentario_formulario(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea)

