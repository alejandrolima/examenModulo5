# Generated by Django 3.1.4 on 2020-12-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20201221_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corresponsal',
            name='biografia',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Biografía'),
        ),
    ]
