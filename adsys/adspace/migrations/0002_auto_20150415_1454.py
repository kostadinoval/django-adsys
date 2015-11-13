# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adspace', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adspace',
            old_name='user_id',
            new_name='user',
        ),
    ]
