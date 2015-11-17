# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151117_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='text',
            field=models.TextField(default='migrations'),
            preserve_default=False,
        ),
    ]
