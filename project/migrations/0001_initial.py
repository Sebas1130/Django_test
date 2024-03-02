# Generated by Django 4.2.10 on 2024-03-02 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('nit', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('tiempo_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('caracteristicas', models.TextField()),
                ('precio_usd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_eur', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_gbp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.producto')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='productos',
            field=models.ManyToManyField(through='project.OrdenProducto', to='project.producto'),
        ),
    ]
