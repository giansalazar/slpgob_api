# Generated by Django 4.1.3 on 2022-11-18 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=60)),
                ('num_ext', models.CharField(max_length=10)),
                ('num_int', models.IntegerField()),
                ('codigo_postal', models.IntegerField()),
                ('localidad', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='Entidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='Jefaturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Jefatura',
                'verbose_name_plural': 'Jefaturas',
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apep', models.CharField(max_length=30, verbose_name='Apellido Paterno')),
                ('apem', models.CharField(max_length=30, verbose_name='Apellido Materno')),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Puestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('jefatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.jefaturas')),
            ],
            options={
                'verbose_name': 'Puesto',
                'verbose_name_plural': 'Puestos',
            },
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.entidades')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado_estudios', models.CharField(max_length=40, verbose_name='Grado de Estudios')),
                ('carrera', models.CharField(max_length=40)),
                ('direccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.direcciones')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personas', verbose_name='Persona')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.puestos', verbose_name='Puesto')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Directorio_Telefonico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=20)),
                ('extension', models.IntegerField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.empleados')),
            ],
            options={
                'verbose_name': 'Directorio',
                'verbose_name_plural': 'Directorio',
            },
        ),
        migrations.AddField(
            model_name='direcciones',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.municipios'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('password', models.CharField(max_length=240)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personas', verbose_name='Persona')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]