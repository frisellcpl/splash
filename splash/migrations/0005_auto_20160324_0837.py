# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splash', '0004_auto_20160324_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleblock',
            name='body',
            field=models.TextField(),
        ),
    ]
