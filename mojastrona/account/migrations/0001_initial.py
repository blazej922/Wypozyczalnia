# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-06-15 14:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrental', '0002_auto_20180615_1403'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.TextField(choices=[(b'reported', b'Zgloszone'), (b'in_progress', b'W trakcie'), (b'done', b'Naprawione')], default=b'reported', max_length=12)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrental.Car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FaultComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fault', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Fault')),
            ],
        ),
        migrations.CreateModel(
            name='Servcie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview_over_date', models.DateField()),
                ('last_oil_change', models.IntegerField()),
                ('isurance', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrental.Car')),
            ],
        ),
    ]
