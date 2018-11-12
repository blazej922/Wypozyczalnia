# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0004_auto_20180711_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='positioninorder',
            name='piosum',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
