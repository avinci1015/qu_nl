# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20151117_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='Bar',
            new_name='bar',
        ),
    ]
