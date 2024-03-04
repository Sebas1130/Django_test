from rest_framework import serializers
from.models import Empresa, Categoria, Producto, Cliente, Orden, OrdenProducto


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nit', 'nombre', 'direccion', 'telefono']
        read_only_fields = ('tiempo_creacion', )

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'caracteristicas', 'precio_usd', 'precio_eur', 'precio_gbp', 'empresa']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido']

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ['productos', 'fecha', 'total', 'cliente']

class OrdenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProducto
        fields = ['orden', 'producto', 'cantidad']
