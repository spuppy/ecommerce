# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.DecimalField(default=10.99, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(default=10.99, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='tax_total',
            field=models.DecimalField(default=0.0, max_digits=1000, decimal_places=2),
            preserve_default=True,
        ),
    ]
