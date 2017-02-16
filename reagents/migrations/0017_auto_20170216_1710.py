# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0016_auto_20170216_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plasmids',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='plasmids',
            unique_together=set([('plasmid_name', 'plasmid_reference', 'supplier', 'lab')]),
        ),
    ]
