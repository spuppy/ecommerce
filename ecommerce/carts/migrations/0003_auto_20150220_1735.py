# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150131_1851'),
        ('carts', '0002_auto_20150220_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=1, to='products.Product'),
            preserve_default=False,
        ),
    ]
