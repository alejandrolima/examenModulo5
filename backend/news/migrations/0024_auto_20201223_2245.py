# Generated by Django 3.1.4 on 2020-12-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20201223_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='etiqueta',
        ),
        migrations.AddField(
            model_name='entrada',
            name='etiqueta',
            field=models.ManyToManyField(blank=True, related_name='entradas', to='news.Etiqueta', verbose_name='Etiqueta'),
        ),
    ]
