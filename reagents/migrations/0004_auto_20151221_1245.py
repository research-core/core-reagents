# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0003_plasmids_plasmid_sequence2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmids',
            name='plasmid_sequence',
            field=models.FileField(upload_to=b'uploads/abstractsequenceinformation', max_length=255, verbose_name=b'Sequence 1'),
            preserve_default=True,
        ),
    ]
