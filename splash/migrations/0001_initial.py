# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=128)),
                ('body', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('tagline', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]