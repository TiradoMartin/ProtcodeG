# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 20:12
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brainstoming',
            fields=[
                ('titulo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descrition', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(max_length=100)),
                ('mensaje', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('titulo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menssege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(max_length=100)),
                ('mensaje', ckeditor.fields.RichTextField(max_length=1000)),
                ('identrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Brainstoming')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='identrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Entrada'),
        ),
    ]
