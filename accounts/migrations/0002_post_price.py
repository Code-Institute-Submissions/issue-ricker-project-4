# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2.5, max_digits=6),
        ),
    ]