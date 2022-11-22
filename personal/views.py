from .models import *
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import *
from .permissions import *

class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonasSerializer


class EmpleadosListadoViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all().order_by('persona__apep')
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadosListadoSerializer


class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all().order_by('persona__apep')
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadosSerializer


class JefaturasViewSet(viewsets.ModelViewSet):
    queryset = Jefaturas.objects.all().order_by('nombre')
    permission_classes = [permissions.AllowAny]
    serializer_class = JefaturasSerializer


class PuestosViewSet(viewsets.ModelViewSet):
    queryset = Puestos.objects.all().order_by('nombre')
    permission_classes = [permissions.AllowAny]
    serializer_class = PuestosSerializer


class EntidadesViewSet(viewsets.ModelViewSet):
    queryset = Entidades.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EntidadesSerializer


class DireccionesViewSet(viewsets.ModelViewSet):
    queryset = Direcciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DireccionesSerializer


class Directorio_TelefonicoViewSet(viewsets.ModelViewSet):
    queryset = Directorio_Telefonico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Directorio_TelefonicoSerializer

class Directorio_TelefonicoBasicViewSet(viewsets.ModelViewSet):
    queryset = Directorio_Telefonico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Directorio_TelefonicoBasicSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]


class UserLoginAPIView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {"request":request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Success'
                    }, status.HTTP_201_CREATED)
                else:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Success'
                    }, status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Credenciales Incorrectas'}, status = status.HTTP_400_BAD_REQUEST)

