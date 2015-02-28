# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amphi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=60, verbose_name='Nom')),
                ('capacity', models.IntegerField(verbose_name='Capacité')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('census', models.IntegerField(verbose_name="Nombre d'éléves présents")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=6, verbose_name='Nom')),
                ('enrolled', models.IntegerField(verbose_name="Nombre d'inscrits")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('number', models.IntegerField(verbose_name='Numéro de la séance')),
                ('course', models.ForeignKey(to='census.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('number', models.IntegerField(verbose_name='Numéro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lesson',
            name='professor',
            field=models.ForeignKey(to='census.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='promotion',
            field=models.ForeignKey(to='census.Promotion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='count',
            name='lesson',
            field=models.ForeignKey(to='census.Lesson'),
            preserve_default=True,
        ),
    ]
