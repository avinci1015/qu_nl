# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151117_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='Bar',
            field=models.ForeignKey(to='core.Bar', null=True),
        ),
    ]
