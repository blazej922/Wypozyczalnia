# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-15 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fault',
            name='car',
        ),
        migrations.RemoveField(
            model_name='fault',
            name='user',
        ),
        migrations.RemoveField(
            model_name='faultcomment',
            name='fault',
        ),
        migrations.RemoveField(
            model_name='servcie',
            name='car',
        ),
        migrations.DeleteModel(
            name='Fault',
        ),
        migrations.DeleteModel(
            name='FaultComment',
        ),
        migrations.DeleteModel(
            name='Servcie',
        ),
    ]
