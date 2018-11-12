# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180615_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='isurance',
            new_name='insurance',
        ),
    ]
