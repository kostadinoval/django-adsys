# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_auto_20150415_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertkeyword',
            old_name='ad_keyword',
            new_name='keyword',
        ),
    ]
