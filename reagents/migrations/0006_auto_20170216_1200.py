# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0005_plasmids_plasmid_sc_enzymes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reagent',
            fields=[
                ('reagent_id', models.AutoField(serialize=False, verbose_name=b'Reagent id', primary_key=True)),
                ('reagent_name', models.CharField(unique=True, max_length=50, verbose_name=b'Name')),
                ('reagent_reagent', models.CharField(max_length=50, verbose_name=b'Reagent')),
                ('reagent_purpose', models.TextField(null=True, verbose_name=b'Purpose', blank=True)),
                ('lab', models.ForeignKey(verbose_name=b'Lab', to='reagents.Lab')),
                ('supplier', models.ForeignKey(verbose_name=b'Supplier', to='reagents.Supplier')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Reagent',
                'verbose_name_plural': 'Reagents',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='antibody',
            name='antibody_ig_class',
            field=models.CharField(help_text=b'(Polyclonal vs. Monoclonal; add IgG class when available)', max_length=50, null=True, verbose_name=b'Ig class', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antibody',
            name='antibody_notes',
            field=models.TextField(null=True, verbose_name=b'Notes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antibody',
            name='antibody_source',
            field=models.CharField(help_text=b'(specie the Ab was raised in; p.e. "Mouse")', max_length=100, null=True, verbose_name=b'Source', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antibody',
            name='antibody_stock_concentration',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Stock Concentration', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antibody',
            name='antibody_working_concentration',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Working concentration', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antibody',
            name='contact',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Person of contact', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antibody',
            name='lab',
            field=models.ForeignKey(default=True, verbose_name=b'Lab', to='reagents.Lab'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemical',
            name='contact',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Person of contact', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enzyme',
            name='contact',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Person of contact', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='contact',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Person of contact', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_attb',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'attB', choices=[(b'N', b'No'), (b'Y', b'Yes')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_backbone',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Backbone', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_flippases',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Flippases', choices=[(b'N', b'No'), (b'Y', b'Yes')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_gateway',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Gateway', choices=[(b'N', b'No'), (b'Y', b'Yes')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_marker',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Marker', choices=[(b'W', b'White gene'), (b'M', b'Mini white gene')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_methylation',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Methylation', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_system',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'System', choices=[(b'G', b'GAL4/UAS'), (b'Q', b'Q'), (b'L', b'LexA')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='plasmid_vector',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Vector', choices=[(b'DO', b'Donor vector'), (b'DE', b'Destination')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='primer',
            name='contact',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Person of contact', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antibody',
            name='antibody_applications',
            field=models.CharField(help_text=b'(p.e. "WB"; "ICC/IF")', max_length=50, null=True, verbose_name=b'Applications', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antibody',
            name='antibody_conjuged2',
            field=models.CharField(help_text=b'(p.e. "Alexa Fluor 488"; "Unconjugated")', max_length=50, verbose_name=b'Conjugated to'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antibody',
            name='antibody_name',
            field=models.CharField(help_text=b'(p.e. "anti-Something")', max_length=50, verbose_name=b'Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antibody',
            name='antibody_prim_sec',
            field=models.CharField(max_length=50, verbose_name=b'Primary/Secondary/Tracer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antibody',
            name='antibody_reactivity',
            field=models.CharField(help_text=b'(species the Ab is know to react to)', max_length=50, verbose_name=b'Reactivity'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='antibody',
            name='antibody_target',
            field=models.CharField(help_text=b'(p.e. "Something")', max_length=50, verbose_name=b'Target'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plasmids',
            name='plasmid_fluorchrome',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Fluorochrome', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plasmids',
            name='plasmid_sequence',
            field=models.FileField(upload_to=b'uploads/abstractsequenceinformation', max_length=255, verbose_name=b'Map'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='plasmids',
            name='plasmid_sequence2',
            field=models.FileField(max_length=255, upload_to=b'uploads/abstractsequenceinformation', null=True, verbose_name=b'Sequence', blank=True),
            preserve_default=True,
        ),
    ]
