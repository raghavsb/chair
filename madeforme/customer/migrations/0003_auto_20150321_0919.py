# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20150307_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyerprofile',
            options={'ordering': ['user'], 'verbose_name': 'buyer', 'verbose_name_plural': 'buyers'},
        ),
        migrations.AlterModelOptions(
            name='makerprofile',
            options={'ordering': ['user'], 'verbose_name': 'maker', 'verbose_name_plural': 'makers'},
        ),
        migrations.AlterField(
            model_name='buyerprofile',
            name='pincode',
            field=models.CharField(default=b'560001', max_length=6),
        ),
    ]
