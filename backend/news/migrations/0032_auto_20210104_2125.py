# Generated by Django 3.1.4 on 2021-01-05 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_auto_20201229_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimedia',
            name='titulo',
            field=models.CharField(max_length=600, null=True, verbose_name='Título'),
        ),
    ]
