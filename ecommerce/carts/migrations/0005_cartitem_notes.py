# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20150221_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
