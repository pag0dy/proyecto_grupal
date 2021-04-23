# Generated by Django 2.2.4 on 2021-04-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registro_acceso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=750)),
                ('fecha_limite', models.DateTimeField(blank=True, null=True)),
                ('recaudacion', models.PositiveSmallIntegerField()),
                ('meta', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agrupacion', models.ManyToManyField(related_name='campana_activa', to='registro_acceso.Agrupacion')),
            ],
        ),
        migrations.CreateModel(
            name='Aporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('aprobado', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aporte_ingresado', to='campana.Campana')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aporte_usuario', to='registro_acceso.Usuario')),
            ],
        ),
    ]
