# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adspace', '0002_auto_20150415_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adspace',
            name='created_on',
        ),
        migrations.AddField(
            model_name='adspace',
            name='datetime_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 11, 52, 6, 807516, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
