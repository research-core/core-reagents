# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0002_auto_20151216_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_sequence2',
            field=models.FileField(max_length=255, upload_to=b'uploads/abstractsequenceinformation', null=True, verbose_name=b'Sequence 2', blank=True),
            preserve_default=True,
        ),
    ]
