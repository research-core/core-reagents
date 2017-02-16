# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0010_auto_20170216_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antibody',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='antibody',
            unique_together=set([('antibody_name', 'antibody_reference', 'supplier', 'lab')]),
        ),
    ]
