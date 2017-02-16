# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0017_auto_20170216_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antibody',
            options={'verbose_name': 'Antibody', 'verbose_name_plural': 'Antibodies'},
        ),
        migrations.AlterModelOptions(
            name='chemical',
            options={'verbose_name': 'Chemical', 'verbose_name_plural': 'Chemicals'},
        ),
        migrations.AlterModelOptions(
            name='enzyme',
            options={'verbose_name': 'Enzyme', 'verbose_name_plural': 'Enzymes'},
        ),
        migrations.AlterModelOptions(
            name='plasmids',
            options={'verbose_name': 'Plasmid', 'verbose_name_plural': 'Plasmids'},
        ),
        migrations.AlterModelOptions(
            name='primer',
            options={'verbose_name': 'Primer', 'verbose_name_plural': 'Primers'},
        ),
    ]
