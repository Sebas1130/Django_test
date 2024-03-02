from rest_framework import routers
from .api import EmpresaViewSet

router = routers.DefaultRouter()

router.register('api/projects', EmpresaViewSet, 'projects')

urlpatterns = router.urls