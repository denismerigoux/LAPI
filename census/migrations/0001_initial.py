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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=60)),
                ('capacity', models.IntegerField(verbose_name='Capacité')),
            ],
            options={
                'verbose_name': 'Amphithéâtre',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('census', models.IntegerField(verbose_name="Nombre d'éléves présents")),
            ],
            options={
                'verbose_name': 'Comptage',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=6)),
                ('enrolled', models.IntegerField(verbose_name="Nombre d'inscrits")),
            ],
            options={
                'verbose_name': 'Cours',
                'verbose_name_plural': 'Cours',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('number', models.IntegerField(verbose_name='Numéro de la séance')),
                ('amphi', models.ForeignKey(verbose_name='Amphithéâtre', to='census.Amphi')),
                ('course', models.ForeignKey(to='census.Course')),
            ],
            options={
                'verbose_name': 'Séance',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nom', max_length=100)),
            ],
            options={
                'verbose_name': 'Professeur',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name='Numéro')),
            ],
            options={
                'verbose_name': 'Promotion',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lesson',
            name='professor',
            field=models.ForeignKey(verbose_name='Professeur', to='census.Professor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='promotion',
            field=models.ForeignKey(verbose_name='Promotion', to='census.Promotion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='count',
            name='lesson',
            field=models.ForeignKey(verbose_name='Séance', to='census.Lesson'),
            preserve_default=True,
        ),
    ]
