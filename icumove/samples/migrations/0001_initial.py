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
                ('side', models.CharField(max_length=1, verbose_name=b'Pump Side', choices=[(b'A', b'Outside of Reception, "Aft"'), (b'B', b'Inside of Reception, "Bow"')])),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'M', b'ILH M-ICU'), (b'T', b'ILH T-ICU'), (b'P', b'UMC T/S-ICU Purple'), (b'O', b'UMC M-ICU Orange'), (b'G', b'UMC Control ICU Green')])),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'M', b'ILH M-ICU'), (b'T', b'ILH T-ICU'), (b'P', b'UMC T/S-ICU Purple'), (b'O', b'UMC M-ICU Orange'), (b'G', b'UMC Control ICU Green')])),
            ],
        ),
        migrations.CreateModel(
            name='Stool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room', models.CharField(max_length=4, verbose_name=b'Room Number')),
                ('emr', models.CharField(max_length=10, verbose_name=b'Epic Medical Record Number)')),
            ],
        ),
    ]
