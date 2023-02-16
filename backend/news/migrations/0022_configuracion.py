# Generated by Django 3.1.4 on 2020-12-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0021_auto_20201223_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre se sección')),
                ('limite', models.IntegerField(verbose_name='Límite de noticias a mostrar')),
            ],
        ),
    ]
