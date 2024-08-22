# Generated by Django 4.2.4 on 2023-11-10 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
        ('productos', '0009_alter_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id_stock', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('fecha_venc', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('numero_lote', models.CharField(max_length=40, verbose_name='N° de LOTE')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.proveedor')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'ordering': ('fecha_venc',),
                'unique_together': {('producto', 'numero_lote')},
            },
        ),
    ]
