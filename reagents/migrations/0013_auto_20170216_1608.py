# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0012_auto_20170216_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='antibody_reactivity',
            field=models.CharField(help_text=b'(species the Ab is know to react to)', max_length=100, verbose_name=b'Reactivity'),
            preserve_default=True,
        ),
    ]
