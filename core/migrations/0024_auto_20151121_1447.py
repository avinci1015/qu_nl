# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='response',
            field=models.ForeignKey(blank=True, to='core.Response', null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='bar',
            field=models.ForeignKey(blank=True, to='core.Bar', null=True),
        ),
    ]
