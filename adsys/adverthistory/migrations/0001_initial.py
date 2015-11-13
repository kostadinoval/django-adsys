# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertClick',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numberOfClicks', models.IntegerField(default=0)),
                ('advert_id', models.ForeignKey(to='advert.Advert')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvertImpression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numberOfImpressions', models.IntegerField(default=0)),
                ('advert_id', models.ForeignKey(to='advert.Advert')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
