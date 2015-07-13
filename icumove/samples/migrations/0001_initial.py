# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('time', models.TimeField(verbose_name=b'Time of Sample')),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'M', b'ILH M-ICU'), (b'T', b'ILH T-ICU'), (b'P', b'UMC T/S-ICU Purple'), (b'O', b'UMC M-ICU Orange'), (b'G', b'UMC Control ICU Green')])),
                ('pump', models.CharField(max_length=1, verbose_name=b'Pump Number', choices=[(b'A', b'ICS Station A'), (b'B', b'ICS Station B'), (b'C', b'ICS Station C'), (b'W', b'Waiting Room')])),
                ('side', models.CharField(max_length=1, verbose_name=b'Pump Side', choices=[(b'1', b'Filter 1'), (b'2', b'Filter 2')])),
                ('day', models.CharField(default=b'00', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('time', models.TimeField(verbose_name=b'Time of Sample')),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'M', b'ILH M-ICU'), (b'T', b'ILH T-ICU'), (b'P', b'UMC T/S-ICU Purple'), (b'O', b'UMC M-ICU Orange'), (b'G', b'UMC Control ICU Green')])),
                ('day', models.CharField(default=b'00', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('time', models.TimeField(verbose_name=b'Time of Sample')),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'M', b'ILH M-ICU'), (b'T', b'ILH T-ICU'), (b'P', b'UMC T/S-ICU Purple'), (b'O', b'UMC M-ICU Orange'), (b'G', b'UMC Control ICU Green')])),
                ('day', models.CharField(default=b'00', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Stool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('time', models.TimeField(verbose_name=b'Time of Sample')),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'M', b'ILH M-ICU'), (b'T', b'ILH T-ICU'), (b'P', b'UMC T/S-ICU Purple'), (b'O', b'UMC M-ICU Orange'), (b'G', b'UMC Control ICU Green')])),
                ('room', models.CharField(max_length=4, verbose_name=b'Room Number')),
                ('pressure', models.CharField(max_length=3, verbose_name=b'Room pressure', choices=[(b'NAN', b'Not Pressured'), (b'NEG', b'Negative Pressure'), (b'POS', b'Positive Pressure')])),
                ('emr', models.CharField(max_length=10, verbose_name=b'Epic Medical Record Number)')),
                ('day', models.CharField(default=b'00', max_length=2)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='stool',
            unique_together=set([('sample_date', 'time', 'icu', 'room', 'emr')]),
        ),
        migrations.AlterUniqueTogether(
            name='floor',
            unique_together=set([('sample_date', 'icu', 'day')]),
        ),
        migrations.AlterUniqueTogether(
            name='door',
            unique_together=set([('sample_date', 'icu', 'day')]),
        ),
        migrations.AlterUniqueTogether(
            name='air',
            unique_together=set([('sample_date', 'icu', 'pump', 'side')]),
        ),
    ]
