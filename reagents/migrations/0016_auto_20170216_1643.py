# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0015_auto_20170216_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enzyme',
            old_name='ensyme_id',
            new_name='enzyme_id',
        ),
    ]
