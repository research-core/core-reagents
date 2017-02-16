# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0014_auto_20170216_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enzyme',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='enzyme',
            unique_together=set([('enzyme_name', 'enzyme_reference', 'supplier', 'lab')]),
        ),
    ]
