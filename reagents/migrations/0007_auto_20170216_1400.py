# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0006_auto_20170216_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemical',
            name='chemical_name',
            field=models.CharField(max_length=50, verbose_name=b'Name'),
            preserve_default=True,
        ),
    ]
