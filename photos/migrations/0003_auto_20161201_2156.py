# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20161201_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.FilePathField(path='photos/images'),
        ),
    ]
