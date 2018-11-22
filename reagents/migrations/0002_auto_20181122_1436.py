# Generated by Django 2.1.3 on 2018-11-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plasmids',
            name='plasmid_temperature',
            field=models.IntegerField(verbose_name='Temperature (C)'),
        ),
        migrations.AlterField(
            model_name='primer',
            name='primer_melting_temp',
            field=models.IntegerField(verbose_name='Melting Temperature (C)'),
        ),
    ]