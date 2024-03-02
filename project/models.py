from django.db import models

# Create your models here.

class Empresa(models.Model):
    nit = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    tiempo_creacion = models.DateTimeField(auto_now_add=True)
    # Otros campos relevantes para la empresa

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos relevantes para la categoría

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    caracteristicas = models.TextField()
    precio_usd = models.DecimalField(max_digits=10, decimal_places=2)
    precio_eur = models.DecimalField(max_digits=10, decimal_places=2)
    precio_gbp = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    # Otros campos relevantes para el producto

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # Otros campos relevantes para el cliente

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Orden(models.Model):
    productos = models.ManyToManyField(Producto, through='OrdenProducto')
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Otros campos relevantes para la orden

    def __str__(self):
        return f"Orden de {self.cliente} - {self.fecha}"

class OrdenProducto(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    # Otros campos relevantes para la relación entre orden y producto

    def __str__(self):
        return f"Orden: {self.orden}, Producto: {self.producto}, Cantidad: {self.cantidad}"