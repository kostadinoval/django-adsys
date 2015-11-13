# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advert',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='advertkeyword',
            old_name='advert_id',
            new_name='advert',
        ),
    ]
