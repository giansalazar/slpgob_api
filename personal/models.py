from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

# Create your models here.
class Personas(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apep = models.CharField(max_length=30, verbose_name="Apellido Paterno")
    apem = models.CharField(max_length=30, verbose_name="Apellido Materno")
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre + self.apep + self.apem
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

class Jefaturas(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Jefatura"
        verbose_name_plural = "Jefaturas"

class Puestos(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"

class Entidades(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"


class Direcciones(models.Model):
    calle = models.CharField(max_length=60)
    """En el número exterior se utiliza la propiedad CharField debido a que hay domicilios que contienen
    letras, ejemplo: 120A"""
    num_ext = models.CharField(max_length=10)
    num_int = models.IntegerField()
    codigo_postal = models.IntegerField()
    localidad = models.CharField(max_length=40)
    municipio = models.CharField(max_length=60)
    entidad = models.ForeignKey(Entidades, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.calle +  self.num_ext
    
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"

class Empleados(models.Model):
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE, verbose_name="Persona")
    puesto = models.ForeignKey(Puestos, on_delete=models.CASCADE, verbose_name="Puesto")
    jefatura = models.ForeignKey(Jefaturas, on_delete=models.CASCADE, null=True)
    grado_estudios = models.CharField(max_length=40, verbose_name="Grado de Estudios")
    carrera = models.CharField(max_length=40)
    direccion = models.ForeignKey(Direcciones, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.persona.nombre

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

class Directorio_Telefonico(models.Model):
    telefono = models.CharField(max_length=10)
    #tipo linea movil o fija
    tipo = models.CharField(max_length=20)
    #la extension es el codigo del pais al que pertenece el número telefonico, ejemplo: en MX es 52
    extension = models.IntegerField()
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

    def __str__(self):
        return self.empleado.persona.nombre +  self.empleado.persona.apep
    
    class Meta:
        verbose_name = "Directorio"
        verbose_name_plural = "Directorio"

class UsuarioManager(BaseUserManager):

    def _create_user(self, username, id_persona_id, email, is_active, is_staff, is_superuser, password):
        if not email:
            raise ValueError("El usuario debe tener un email")
        
        usuario = self.model(username=username, id_persona_id=id_persona_id, email=self.normalize_email(email), is_active=is_active, is_staff=is_staff, is_superuser=is_superuser)

        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario
    
    def create_user(self, username, id_persona_id, email, password):
        return self._create_user(username, id_persona_id, email, True, True, False, password)
    
    def create_superuser(self, username, email, id_persona_id, password):
        
        usuario=self.create_user(username=username, id_persona_id=id_persona_id, email=email, password=password)

        usuario.is_superuser=True

        usuario.save()

        return usuario
    

class Usuario(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(verbose_name="Usuario", max_length=20, unique=True)
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE, verbose_name="Persona")
    email = models.EmailField(verbose_name="Email")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    password = models.CharField(max_length=240)
    objects=UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'email','id_persona_id'