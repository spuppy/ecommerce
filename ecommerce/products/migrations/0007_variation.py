# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150131_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(null=True, max_digits=100, decimal_places=2, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ForeignKey(blank=True, to='products.ProductImage', null=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
