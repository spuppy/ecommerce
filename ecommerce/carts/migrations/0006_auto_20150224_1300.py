# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_variation_category'),
        ('carts', '0005_cartitem_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(to='products.Variation', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
