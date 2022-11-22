from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('api/personas', PersonasViewSet, 'personas')
router.register('api/empleadosListado', EmpleadosListadoViewSet, 'empleadosListado')
router.register('api/empleados', EmpleadosViewSet, 'empleados')
router.register('api/jefaturas', JefaturasViewSet, 'jefaturas')
router.register('api/puestos', PuestosViewSet, 'puestos')
router.register('api/entidades', EntidadesViewSet, 'entidades')
router.register('api/direcciones', DireccionesViewSet, 'direcciones')
router.register('api/directorio', Directorio_TelefonicoViewSet, 'directorio')
router.register('api/directorio_basic', Directorio_TelefonicoBasicViewSet, 'directorio_basic')
router.register('api/usuarios', UsuarioViewSet, 'usuarios')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginAPIView.as_view()),
]
