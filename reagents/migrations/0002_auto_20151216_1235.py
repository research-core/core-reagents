# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmids',
            name='plasmid_temperature',
            field=models.IntegerField(max_length=3, verbose_name=b'Temperature (C)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='primer',
            name='primer_melting_temp',
            field=models.IntegerField(max_length=3, verbose_name=b'Melting Temperature (C)'),
            preserve_default=True,
        ),
    ]
