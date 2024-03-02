from rest_framework import viewsets, permissions
from .models import Empresa
from .serializers import EmpresaSerializer



# class EmpresaViewSet(viewsets.ModelViewSet):
#     queryset = Empresa.objects.all()
#     permission_classes = [permissions.AllowAny]


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer