from rest_framework import viewsets, permissions
from .models import Empresa, Categoria, Producto, Cliente, Orden, OrdenProducto
from .serializers import EmpresaSerializer, CategoriaSerializer, ProductoSerializer, ClienteSerializer, OrdenSerializer, OrdenProductoSerializer

# Autenticacion para los viewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes

@authentication_classes([TokenAuthentication])
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenProductoViewSet(viewsets.ModelViewSet):
    queryset = OrdenProducto.objects.all()
    serializer_class = OrdenProductoSerializer
