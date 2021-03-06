# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nome')),
                ('slug', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('thumbnail', models.ImageField(upload_to='C:\\wamp64\\www\\ifs\\vulnerabilidades\\hotsite\\hotsite\\core\\media', verbose_name='Imagem Destacada')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Category', verbose_name='Categoria')),
            ],
        ),
    ]
