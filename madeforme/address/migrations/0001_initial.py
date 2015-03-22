# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20150321_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20, choices=[(b'BLR', b'Bangalore'), (b'BOM', b'Mumbai'), (b'MAD', b'Chennai')])),
                ('state', models.CharField(max_length=20, choices=[(b'KR', b'Karnataka'), (b'MH', b'Maharashtra'), (b'TN', b'Tamil Nadu')])),
                ('pincode', models.CharField(default=b'560001', max_length=6)),
                ('buyer', models.OneToOneField(to='customer.BuyerProfile')),
            ],
            options={
                'ordering': ['buyer'],
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
            bases=(models.Model,),
        ),
    ]
