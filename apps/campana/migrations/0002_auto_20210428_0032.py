# Generated by Django 2.2.4 on 2021-04-28 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campana', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aporte',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campana',
            name='meta',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campana',
            name='recaudacion',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
