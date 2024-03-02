from rest_framework import serializers
from.models import Empresa, Producto


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nit', 'nombre', 'direccion', 'telefono']
        read_only_fields = ('tiempo_creacion', )



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['__all__']
