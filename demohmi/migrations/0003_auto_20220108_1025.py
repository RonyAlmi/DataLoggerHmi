# Generated by Django 3.2.8 on 2022-01-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demohmi', '0002_auto_20211126_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valores',
            name='descripcion',
            field=models.TextField(verbose_name='descrpcion'),
        ),
        migrations.AlterField(
            model_name='valores',
            name='parametros',
            field=models.CharField(max_length=100, verbose_name='parametros'),
        ),
    ]
