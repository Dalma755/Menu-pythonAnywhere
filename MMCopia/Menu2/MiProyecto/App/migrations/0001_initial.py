# Generated by Django 5.1.2 on 2024-10-11 12:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_mesa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('adicional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='CafeTe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('adicional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('adicional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Guarnicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('adicional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('adicional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.FloatField(default=0.0)),
                ('entregado', models.BooleanField(default=False)),
                ('bebida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.bebida')),
                ('cafe_te', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.cafete')),
                ('guarnicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.guarnicion')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.mesa')),
                ('plato_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.comida')),
                ('postre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.postre')),
            ],
        ),
    ]