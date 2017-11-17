# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-17 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_software_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='software',
            name='licenses_number',
            field=models.CharField(default='-', max_length=25, verbose_name='Número de licenças'),
        ),
        migrations.AlterField(
            model_name='software',
            name='note',
            field=models.TextField(verbose_name='Observações'),
        ),
    ]
