# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AntibioticResistance',
            fields=[
                ('antibioticresistance_id', models.AutoField(serialize=False, verbose_name=b'Antibiotic resistance id', primary_key=True)),
                ('antibioticresistance_name', models.CharField(unique=True, max_length=100, verbose_name=b'Antibiotic resistence name')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Antibiotic resistance',
                'verbose_name_plural': 'Antibiotic Resistances',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Antibody',
            fields=[
                ('antibody_id', models.AutoField(serialize=False, verbose_name=b'Antibody id', primary_key=True)),
                ('antibody_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('antibody_target', models.CharField(max_length=50, verbose_name=b'Target')),
                ('antibody_prim_sec', models.CharField(max_length=50, verbose_name=b'Primary/Secondary')),
                ('antibody_conjuged2', models.CharField(max_length=50, verbose_name=b'Conjugated to')),
                ('antibody_reactivity', models.CharField(max_length=50, verbose_name=b'Reactivity')),
                ('antibody_reference', models.CharField(max_length=50, verbose_name=b'Reference')),
                ('antibody_description', models.CharField(max_length=50, null=True, verbose_name=b'Description', blank=True)),
                ('antibody_applications', models.CharField(max_length=50, null=True, verbose_name=b'Applications', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Antibody',
                'verbose_name_plural': 'Antibodies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('chemical_id', models.AutoField(serialize=False, verbose_name=b'Chemical id', primary_key=True)),
                ('chemical_name', models.CharField(unique=True, max_length=50, verbose_name=b'Name')),
                ('chemical_formula', models.CharField(max_length=50, verbose_name=b'Formula')),
                ('chemical_purpose', models.TextField(null=True, verbose_name=b'Purpose', blank=True)),
                ('chemical_reference', models.CharField(max_length=50, verbose_name=b'Reference')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Chemical',
                'verbose_name_plural': 'Chemicals',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enzyme',
            fields=[
                ('ensyme_id', models.AutoField(serialize=False, verbose_name=b'Enzyme id', primary_key=True)),
                ('enzyme_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('enzyme_description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('enzyme_reference', models.CharField(max_length=50, verbose_name=b'Reference')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Enzyme',
                'verbose_name_plural': 'Enzymes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EnzymeType',
            fields=[
                ('enzymetype_id', models.AutoField(serialize=False, verbose_name=b'Enzyme type id', primary_key=True)),
                ('enzymetype_name', models.CharField(unique=True, max_length=100, verbose_name=b'Enzyme type name')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Enzyme type',
                'verbose_name_plural': 'Enzymes types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GrowthStrains',
            fields=[
                ('growthstrain_id', models.AutoField(serialize=False, verbose_name=b'Growth strain id', primary_key=True)),
                ('growthstrain_name', models.CharField(unique=True, max_length=100, verbose_name=b'Growth strain name')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Growth strain',
                'verbose_name_plural': 'Growth strains',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.AutoField(serialize=False, verbose_name=b'Lab id', primary_key=True)),
                ('lab_name', models.CharField(max_length=100, verbose_name=b'Lab name')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Lab',
                'verbose_name_plural': 'Labs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plasmids',
            fields=[
                ('plasmid_id', models.AutoField(serialize=False, verbose_name=b'Plasmid id', primary_key=True)),
                ('plasmid_name', models.CharField(max_length=50, verbose_name=b'Plasmid name')),
                ('plasmid_mcs', models.BooleanField(default=False, verbose_name=b'Multiple Cloning Site (MCS)')),
                ('plasmid_reference', models.CharField(max_length=50, verbose_name=b'Reference')),
                ('plasmid_promoter', models.CharField(max_length=50, verbose_name=b'Promoter')),
                ('plasmid_transgene', models.CharField(max_length=50, verbose_name=b'Transgene')),
                ('plasmid_fluorchrome', models.CharField(max_length=50, verbose_name=b'Fluorchrome')),
                ('plasmid_seq_primers', models.CharField(max_length=50, verbose_name=b'Sequencing primers')),
                ('plasmid_sequence', models.FileField(upload_to=b'uploads/abstractsequenceinformation', max_length=255, verbose_name=b'Sequence')),
                ('plasmid_temperature', models.DecimalField(verbose_name=b'Temperature (C)', max_digits=5, decimal_places=2)),
                ('anti_resistance', models.ForeignKey(verbose_name=b'Antibiotic resistance', to='reagents.AntibioticResistance')),
                ('growthstrain', models.ForeignKey(verbose_name=b'Growth strain', blank=True, to='reagents.GrowthStrains', null=True)),
                ('lab', models.ForeignKey(verbose_name=b'Lab', to='reagents.Lab')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Plasmid',
                'verbose_name_plural': 'Plasmids',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Primer',
            fields=[
                ('primer_id', models.AutoField(serialize=False, verbose_name=b'Primer id', primary_key=True)),
                ('primer_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('primer_sequence', models.CharField(max_length=100, verbose_name=b"Sequence (5'-3')")),
                ('primer_purpose', models.TextField(verbose_name=b'Purpose')),
                ('primer_melting_temp', models.DecimalField(verbose_name=b'Melting Temperature (C)', max_digits=3, decimal_places=2)),
                ('lab', models.ForeignKey(verbose_name=b'Lab', to='reagents.Lab')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Primer',
                'verbose_name_plural': 'Primers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(serialize=False, verbose_name=b'Supplier id', primary_key=True)),
                ('supplier_name', models.CharField(unique=True, max_length=100, verbose_name=b'Supplier name')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VectorType',
            fields=[
                ('vectortype_id', models.AutoField(serialize=False, verbose_name=b'Vector type id', primary_key=True)),
                ('vectortype_name', models.CharField(unique=True, max_length=100, verbose_name=b'Vector type name')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Vector type',
                'verbose_name_plural': 'Vector types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='primer',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'Supplier', to='reagents.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'Supplier', to='reagents.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plasmids',
            name='vectortype',
            field=models.ForeignKey(verbose_name=b'Vector type', to='reagents.VectorType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enzyme',
            name='enzymetype',
            field=models.ForeignKey(verbose_name=b'Type of enzyme', to='reagents.EnzymeType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enzyme',
            name='lab',
            field=models.ForeignKey(verbose_name=b'Lab', to='reagents.Lab'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='enzyme',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'Supplier', to='reagents.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemical',
            name='lab',
            field=models.ForeignKey(verbose_name=b'Lab', to='reagents.Lab'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chemical',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'Supplier', to='reagents.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='antibody',
            name='supplier',
            field=models.ForeignKey(verbose_name=b'Supplier', to='reagents.Supplier'),
            preserve_default=True,
        ),
    ]
