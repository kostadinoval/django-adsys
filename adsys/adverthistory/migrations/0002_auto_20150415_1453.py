# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverthistory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertclick',
            old_name='advert_id',
            new_name='advert',
        ),
        migrations.RenameField(
            model_name='advertimpression',
            old_name='advert_id',
            new_name='advert',
        ),
    ]
