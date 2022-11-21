from django.contrib import admin
from .models import *

# Register your models here.

class PersonasAdmin(admin.ModelAdmin):
    list_display = ('nombre','apep', 'apem',)
    search_fields = ('nombre','apep', 'apem',)

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('persona','puesto', 'jefatura', 'direccion')
    search_fields = ('persona.nombre','persona.apep', 'persona.apem',)

class PuestosAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class JefaturasAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class DireccionesAdmin(admin.ModelAdmin):
    list_display = ('calle', 'codigo_postal', 'localidad', 'municipio')
    search_fields = ('calle', 'codigo_postal', 'localidad', 'municipio.nombre', )

class EntidadsAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class Directorio_TelefonicoAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'tipo', 'extension', 'empleado')
    search_fields = ('telefono', 'tipo', 'extension', 'empleado')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_persona','username', 'email', 'is_staff')
    search_fields = ('username', 'email')

admin.site.register(Personas, PersonasAdmin)
admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(Puestos, PuestosAdmin)
admin.site.register(Jefaturas, JefaturasAdmin)
admin.site.register(Direcciones, DireccionesAdmin)
admin.site.register(Entidades, EntidadsAdmin)
admin.site.register(Directorio_Telefonico, Directorio_TelefonicoAdmin)
admin.site.register(Usuario, UsuarioAdmin)