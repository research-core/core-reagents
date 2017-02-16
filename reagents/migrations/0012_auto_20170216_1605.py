# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0011_auto_20170216_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='antibody_name',
            field=models.CharField(help_text=b'(p.e. "anti-Something")', max_length=100, verbose_name=b'Name'),
            preserve_default=True,
        ),
    ]
