# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20151117_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='Bar',
            field=models.ForeignKey(default=1, to='core.Bar'),
            preserve_default=False,
        ),
    ]
