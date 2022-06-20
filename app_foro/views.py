from django.shortcuts import  render
from app_foro.models import publicacion , contacto , sorteo , avatar,comentario
from django.db.models import Q
from app_foro.forms import Sorteo_formulario,Publicacion_formulario, Contacto_formulario, UserEditForm, UserRegisterForm,Comentario_formulario
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

def Home(request):
    return render(request , 'home.html')
    
def Contacto(request):
    return render(request , 'contacto/contacto.html')

def Nosotros(request):
    return render(request , 'acerca_de_nosotros.html')

@login_required
def Publicacion(request):
    return render(request , 'publicacion/publicacion_foro.html')

def Busqueda(request):
    return render(request , 'busqueda/busqueda.html')

def Sorteo(request):
    return render(request , 'sorteo/sorteo.html')

def Formulario_publicacion(request):
    if request.method == "POST":
        
        formulario_publicaion = Publicacion_formulario(request.POST)
        if formulario_publicaion.is_valid():
            datos = formulario_publicaion.cleaned_data

            datos_publicacion = publicacion(usuario = datos['usuario'] , tema_especifico = datos['tema_especifico'] , consulta = datos['consulta'] , fecha_de_publicacion = datetime.now())
            datos_publicacion.save()
            return render (request , 'publicacion/publicacion_confirmada.html')
        
        else:
            return render (request , 'publicacion/publicacion_rechazada.html')
            
       
    return render (request, 'publicacion/publicacion_foro.html')
       
def Formulario_contacto(request):
    if request.method == "POST":
        
        formulario_contacto = Contacto_formulario(request.POST)
        if formulario_contacto.is_valid():
            
            datos = formulario_contacto.cleaned_data

            datos_contactante = contacto(usuario = datos['usuario'] , email = datos['email'] , razon_contacto = datos['razon_contacto'] , fecha_de_contacto = datetime.now() )
            datos_contactante.save()
            return render(request , 'contacto/contacto_confirmado.html')
        
        else:
            return render(request , 'contacto/rechazo_contacto.html')
    
    return render(request,'contacto/contacto.html')

def Formulario_sorteo(request):
    if request.method == "POST":

        formulario_sorteo = Sorteo_formulario(request.POST)
        if formulario_sorteo.is_valid():
            
            datos = formulario_sorteo.cleaned_data

            datos_sorteo = sorteo(nombre = datos['nombre'] , apellido = datos['apellido'] , email = datos['email'] , telefono = datos['telefono'])
            datos_sorteo.save()
            return render (request , 'sorteo/sorteo_confirmado.html')
        else:
            return render(request, 'sorteo/rechazo_sorteo.html')


        
            
    return render(request , 'sorteo/sorteo.html')

def Formulario_buscador(request):
    
    if request.GET["texto"]:
        buscador = request.GET["texto"]
        resultado = publicacion.objects.filter(Q(id__icontains = buscador) | Q(usuario__icontains = buscador) | Q(tema_especifico__icontains=buscador) | Q(consulta__icontains=buscador))
    
        
        return render(request , 'busqueda/resultado_busqueda.html' , {'resultado':resultado})

def Formulario_comentario(request):
   
    if request.method == "POST":

        formulario_comentario = Comentario_formulario(request.POST)
        if formulario_comentario.is_valid():
            datos = formulario_comentario.cleaned_data
            datos_comentario = comentario(comentario = datos['respuesta'])
            datos_comentario.save()
            return render(request , 'publicacion/respuesta_confirmada.html')
    
    return render(request , 'comentario/responder_publicacion.html')

@login_required    
def Borrar_publicacion(request , id):
    
    Publicacion = publicacion.objects.get(id=id)
    Publicacion.delete()

    

    return render(request , 'busqueda/publicacion_borrada.html')

@login_required
def Editar_publicacion(request , id):

    Publicacion = publicacion.objects.get(id=id)

    if request.method == "POST":

        publicacion_formulario = Publicacion_formulario( request.POST ) 
        if publicacion_formulario.is_valid():
            datos = publicacion_formulario.cleaned_data
            Publicacion.usuario = datos['usuario']
            Publicacion.tema_especifico = datos['tema_especifico']
            Publicacion.consulta = datos['consulta']
            Publicacion.save()

            return render (request , 'publicacion/edicion_confirmada.html')
    
    else:
        publicacion_formulario = Publicacion_formulario(initial= {'usuario':publicacion.usuario , 'tema_especifico':publicacion.tema_especifico , 'consulta':publicacion.consulta})
    
    return render (request , 'publicacion/editar_publicacion.html' , {'publicacion_formulario':publicacion_formulario , 'Publicacion':Publicacion})

def Vista_Publicacion(request , id):
    Publicacion = publicacion.objects.get(id=id)
    return render(request , 'publicacion/vista_publicacion.html',{'Publicacion':Publicacion})

def Login(request):
    
    if request.method == "POST":

        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = usuario , password = password)

            if user is not None:
                login(request , user)
                avatares = avatar.objects.filter(user=request.user.id)
                if avatares:
                    return render(request , 'usuario/login_confirmado.html',{'url':avatares[0].imagen.url})
                else:
                    return render(request , 'usuario/login_confirmado.html')

            else:
                return render(request , 'usuario/usuario_incorrecto.html')

        else:
            return render(request , 'usuario/error_login.html' ,{'form':form})

    form = AuthenticationForm()

    return render(request , 'usuario/login.html',{'form':form})

def Registro(request):
    
    if request.method == 'POST':
        formulario_registro = UserRegisterForm (request.POST)
        if formulario_registro.is_valid():

            username = formulario_registro.cleaned_data['username']
            formulario_registro.save()
            return render (request , 'usuario/bienvenida_usuario.html')
        
    else:
        formulario_registro = UserRegisterForm()
        
    return render(request , 'usuario/registro_usuario.html' , {'formulario_registro' : formulario_registro})
    
@login_required
def Editar_usuario(request):

    usuario = request.user
    if request.method == "POST":

        formulario_edicion = UserEditForm(request.POST)
        if formulario_edicion.is_valid():
            datos = formulario_edicion.cleaned_data
            usuario.username = datos['username']
            usuario.email = datos['email']
            password = datos['password1']
            usuario.set_password(password)
            usuario.save()

            return render (request , 'usuario/edicion_confirmada.html')

    else:
        formulario_edicion = UserEditForm(initial={'email':usuario.email})
    
    return render(request , 'usuario/editar_usuario.html' , {'formulario_edicion':formulario_edicion , 'usuario':usuario})

def Blog(request):
    datos = publicacion.objects.all()
    return render(request , 'blog.html' , {'datos':datos})

def Responder_Publicacion(request , id):
    Publicacion = publicacion.objects.get(id=id)
    return render(request , 'comentario/responder_publicacion.html',{'Publicacion':Publicacion})



