# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0004_auto_20151221_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_sc_enzymes',
            field=models.TextField(null=True, verbose_name=b'Single cutting enzymes', blank=True),
            preserve_default=True,
        ),
    ]
