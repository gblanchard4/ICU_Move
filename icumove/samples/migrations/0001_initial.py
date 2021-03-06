# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('time', models.IntegerField(verbose_name=b'Hour of Sample (24-hour Clock', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'1', b'UMC Tower-1'), (b'2', b'UMC Tower-2'), (b'3', b'UMC Tower-3')])),
                ('color', models.CharField(max_length=1, verbose_name=b'Tape Color', choices=[(b'R', b'Red'), (b'G', b'Green'), (b'B', b'Blue')])),
                ('pump', models.CharField(max_length=1, verbose_name=b'Pump Number', choices=[(b'A', b'ICS Station A'), (b'B', b'ICS Station B'), (b'C', b'ICS Station C'), (b'E', b'Outdoor')])),
                ('side', models.CharField(max_length=1, verbose_name=b'Pump Side', choices=[(b'1', b'Filter 1'), (b'2', b'Filter 2')])),
                ('rack', models.CharField(max_length=2, verbose_name=b'Freezer Rack', blank=True)),
                ('shelf', models.CharField(max_length=2, verbose_name=b'Shelf', blank=True)),
                ('box', models.CharField(max_length=2, verbose_name=b'Box', blank=True)),
                ('day', models.CharField(default=b'00', max_length=2)),
                ('uid', models.CharField(max_length=16, unique=True, serialize=False, primary_key=True)),
                ('notes', models.TextField(verbose_name=b'Notes', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('time', models.IntegerField(verbose_name=b'Hour of Sample (24-hour Clock', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'1', b'UMC Tower-1'), (b'2', b'UMC Tower-2'), (b'3', b'UMC Tower-3')])),
                ('pump', models.CharField(max_length=1, verbose_name=b'Pump Number', choices=[(b'A', b'ICS Station A'), (b'B', b'ICS Station B'), (b'C', b'ICS Station C'), (b'E', b'Outdoor')])),
                ('side', models.CharField(max_length=1, verbose_name=b'Pump Side', choices=[(b'1', b'Filter 1'), (b'2', b'Filter 2')])),
                ('humidity', models.IntegerField(verbose_name=b'Percent Relative Humidity', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('temp', models.IntegerField(verbose_name=b'Temperature in F???', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('pressure', models.IntegerField(verbose_name=b'Barometric Pressure', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('day', models.CharField(default=b'00', max_length=2)),
                ('uid', models.CharField(max_length=16, unique=True, serialize=False, primary_key=True)),
                ('notes', models.TextField(verbose_name=b'Notes', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stool',
            fields=[
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('time', models.IntegerField(verbose_name=b'Hour of Sample (24-hour Clock', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)])),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'M', b'ILH M-ICU'), (b'T', b'ILH T-ICU'), (b'1', b'UMC Tower-1'), (b'2', b'UMC Tower-2'), (b'3', b'UMC Tower-3')])),
                ('room', models.CharField(max_length=4, verbose_name=b'Room Number')),
                ('emr', models.CharField(max_length=10, verbose_name=b'Epic Medical Record Number')),
                ('rack', models.CharField(max_length=2, verbose_name=b'Freezer Rack', blank=True)),
                ('shelf', models.CharField(max_length=2, verbose_name=b'Shelf', blank=True)),
                ('box', models.CharField(max_length=2, verbose_name=b'Box', blank=True)),
                ('day', models.CharField(default=b'00', max_length=2)),
                ('uid', models.CharField(max_length=27, unique=True, serialize=False, primary_key=True)),
                ('pressure', models.CharField(max_length=3, verbose_name=b'Room pressure', choices=[(b'NAN', b'Not Pressured'), (b'NEG', b'Negative Pressure'), (b'POS', b'Positive Pressure')])),
                ('notes', models.TextField(verbose_name=b'Notes', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('sample_date', models.DateField(verbose_name=b'Sample Date')),
                ('icu', models.CharField(max_length=1, verbose_name=b'ICU Location', choices=[(b'1', b'UMC Tower-1'), (b'2', b'UMC Tower-2'), (b'3', b'UMC Tower-3')])),
                ('room', models.CharField(max_length=4, verbose_name=b'Room Number')),
                ('rack', models.CharField(max_length=2, verbose_name=b'Freezer Rack', blank=True)),
                ('shelf', models.CharField(max_length=2, verbose_name=b'Shelf', blank=True)),
                ('box', models.CharField(max_length=2, verbose_name=b'Box', blank=True)),
                ('day', models.CharField(default=b'00', max_length=2)),
                ('uid', models.CharField(max_length=16, unique=True, serialize=False, primary_key=True)),
                ('notes', models.TextField(verbose_name=b'Notes', blank=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='toilet',
            unique_together=set([('icu', 'room', 'sample_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='stool',
            unique_together=set([('sample_date', 'time', 'icu', 'room', 'emr')]),
        ),
        migrations.AlterUniqueTogether(
            name='environment',
            unique_together=set([('sample_date', 'icu', 'pump', 'side')]),
        ),
        migrations.AlterUniqueTogether(
            name='air',
            unique_together=set([('rack', 'shelf', 'box')]),
        ),
    ]
