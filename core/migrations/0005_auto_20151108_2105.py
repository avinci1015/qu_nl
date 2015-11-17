# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151108_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='text',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
    ]
