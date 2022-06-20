from django.contrib import admin
from app_foro.models import *


# Register your models here.


class display_publicaciones(admin.ModelAdmin):
    list_display = ('usuario'  , 'tema_especifico' , 'consulta' , 'fecha_de_publicacion')
    list_filter = ('tema_especifico' , )
    search_fields = ('consulta' , )


class display_contacto(admin.ModelAdmin):
    list_display = ('usuario' , 'email' , 'razon_contacto' , 'fecha_de_contacto')
    search_fields = ('usuario' , )


class display_sorteo(admin.ModelAdmin):
    list_display = ('nombre' , 'apellido' , 'email' , 'telefono')
    list_filter = ('nombre' , 'apellido')
    search_fields = ('apellido' , )
    

admin.site.register(publicacion , display_publicaciones)
admin.site.register(contacto , display_contacto)
admin.site.register(sorteo , display_sorteo)
admin.site.register(avatar)


