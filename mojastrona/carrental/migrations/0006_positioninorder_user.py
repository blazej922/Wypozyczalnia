# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrental', '0005_positioninorder_piosum'),
    ]

    operations = [
        migrations.AddField(
            model_name='positioninorder',
            name='user',
            field=models.ForeignKey(default=20, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
