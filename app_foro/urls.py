
from django.urls import path
from app_foro import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('' , views.Home),
    path('home' , views.Home , name= 'home'),
    path('contacto' , views.Contacto , name= 'contacto'),
    path('nosotros' , views.Nosotros , name= 'nosotros'),
    path('publicacion' , views.Publicacion , name= 'publicacion'),
    path('busqueda' , views.Busqueda , name= 'busqueda'),
    path('sorteo' , views.Sorteo , name= 'sorteo'),
    path('formulario_buscador' , views.Formulario_buscador),
    path('formulario_publicacion' , views.Formulario_publicacion , name= 'formulario_publicacion'),
    path('formulario_sorteo' , views.Formulario_sorteo , name='formulario_sorteo'),
    path('formulario_contacto' , views.Formulario_contacto , name='formulario_contacto'),
    path('formulario_comentario' , views.Formulario_comentario , name='formulario_comentario'),
    path('borrar_publicacion/<int:id>' , views.Borrar_publicacion , name='borrar_publicacion'),
    path('borrar_publicacion/home' , views.Home),
    path('borrar_publicacion/busqueda' , views.Busqueda),
    path('editar_publicacion/<int:id>' , views.Editar_publicacion, name='editar_publicacion'),
    path('editar_publicacion' , views.Editar_publicacion, name='editar_publicacion'),
    path('login' , views.Login , name='login'),
    path('registro' , views.Registro , name='registro'),
    path('logout' , LogoutView.as_view(template_name = 'usuario/logout.html') , name='logout'),
    path('editar_usuario' , views.Editar_usuario , name='editar_usuario'),
    path('blog' , views.Blog , name='blog'),
    path('vista_publicacion/<int:id>' , views.Vista_Publicacion , name='vista_publicacion'),
    path('responder_publicacion/<int:id>' , views.Responder_Publicacion , name='responder_publicacion'),
    


    




] 