# Generated by Django 2.1.8 on 2019-06-03 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0003_lab_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('virus_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Virus id')),
                ('virus_name', models.CharField(max_length=50, verbose_name='Name')),
                ('virus_serotype', models.CharField(blank=True, max_length=50, null=True, verbose_name='Serotype')),
                ('virus_titter', models.CharField(max_length=50, verbose_name='Titter')),
                ('virus_dna_available', models.CharField(blank=True, choices=[('N', 'No'), ('Y', 'Yes')], max_length=10, null=True, verbose_name='DNA available')),
                ('virus_reference', models.CharField(max_length=50, verbose_name='Reference')),
                ('contact', models.CharField(blank=True, max_length=100, null=True, verbose_name='Person of contact')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Lab', verbose_name='Lab')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.Supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Virus',
                'verbose_name_plural': 'Viruses',
            },
        ),
        migrations.CreateModel(
            name='VirusType',
            fields=[
                ('virustype_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Virus type id')),
                ('virustype_name', models.CharField(max_length=100, unique=True, verbose_name='Virus type name')),
            ],
            options={
                'verbose_name': 'Virus type',
                'verbose_name_plural': 'Viruses types',
            },
        ),
        migrations.AddField(
            model_name='virus',
            name='virus_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reagents.VirusType', verbose_name='Virus type'),
        ),
        migrations.AlterUniqueTogether(
            name='virus',
            unique_together={('virus_name', 'virus_reference', 'supplier', 'lab')},
        ),
    ]
