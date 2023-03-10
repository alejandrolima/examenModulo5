# Generated by Django 3.1.4 on 2020-12-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_entrada_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='multimedia',
            name='descargas',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Descargas'),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='visitas',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Visitas'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='visitas',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Visitas'),
        ),
    ]
