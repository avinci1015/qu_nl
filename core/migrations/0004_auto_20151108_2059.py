# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
