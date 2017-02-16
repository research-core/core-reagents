# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0008_auto_20170216_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chemical',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='chemical',
            unique_together=set([('chemical_name', 'supplier', 'lab')]),
        ),
    ]
