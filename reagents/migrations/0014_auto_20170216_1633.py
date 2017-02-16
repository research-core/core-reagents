# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0013_auto_20170216_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='primer',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='primer',
            unique_together=set([('primer_name', 'primer_sequence', 'supplier', 'lab')]),
        ),
    ]
