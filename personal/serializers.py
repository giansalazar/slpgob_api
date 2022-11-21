from rest_framework import serializers
from .models import *

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ('id','nombre', 'apep', 'apem', 'edad', 'genero')


class JefaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jefaturas
        fields = ('id','nombre',)


class PuestosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puestos
        fields = ('id','nombre',)


class EntidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidades
        fields = ('nombre', )
        

class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = ('id','calle', 'num_ext', 'num_int', 'codigo_postal', 'localidad', 'municipio')

class EmpleadosListadoSerializer(serializers.ModelSerializer):

    #a los campos de llaves foraneas les asignamos el serializador correspondiente para anidar la información
    persona = PersonasSerializer()
    direccion = DireccionesSerializer()
    puesto = PuestosSerializer()
    jefatura = JefaturasSerializer()

    class Meta:
        model = Empleados
        fields = ('id','persona', 'puesto', 'jefatura','carrera', 'grado_estudios', 'direccion',)

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id','persona', 'puesto', 'jefatura','carrera', 'grado_estudios', 'direccion',)
        

class Directorio_TelefonicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ('telefono', 'tipo', 'extension', 'empleado', )


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','username', 'id_persona', 'email', 'password', )
        extra_kwargs = {'password': {
            'write_only': True,
            'style': {'input_type':'password'}
        }}

    def update(self, instance, validated_data):
        #Creamos y retornamos un nuevo un usuario
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)


class UserTokenSerializer(serializers.ModelSerializer):
    id_persona = PersonasSerializer()

    class Meta:
        model = Usuario
        fields = ('id','username', 'id_persona', 'email', )