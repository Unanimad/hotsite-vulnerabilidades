# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20171019_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.TypeUse', verbose_name='Tipo de uso'),
        ),
    ]
