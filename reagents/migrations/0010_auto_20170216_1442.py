# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0009_auto_20170216_1430'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chemical',
            unique_together=set([('chemical_name', 'chemical_reference', 'supplier', 'lab')]),
        ),
    ]
