# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pageURL', models.URLField()),
                ('has_adscore', models.BooleanField(default=False)),
                ('text', models.TextField(default=b'')),
                ('crawl_date', models.DateTimeField(auto_now_add=True)),
                ('domain', models.ForeignKey(to='domain.Domain')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
