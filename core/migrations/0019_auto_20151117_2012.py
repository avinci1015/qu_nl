# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20151117_2012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='bar',
            new_name='Bar',
        ),
    ]
