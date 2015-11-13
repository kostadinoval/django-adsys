# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_auto_20150415_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='date_posted',
        ),
        migrations.AddField(
            model_name='advert',
            name='datetime_posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 16, 10, 54, 28, 317681, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
