from rest_framework import routers
from .api import EmpresaViewSet, ProjectsViewSet, ClienteViewSet, OrdenViewSet, OrdenProductoViewSet, CategoriaViewSet
from . import views
from django.urls import path, include

router = routers.DefaultRouter()


router.register('api/empresa', EmpresaViewSet, 'empresa')
router.register('api/categoria', CategoriaViewSet, 'categoria')
router.register('api/projects', ProjectsViewSet, 'projects')
router.register('api/cliente', ClienteViewSet, 'cliente')
router.register('api/orden', OrdenViewSet, 'orden')
router.register('api/ordenProducto', OrdenProductoViewSet, 'ordenProducto')

urlpatterns = router.urls