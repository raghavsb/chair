# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pincode', models.CharField(max_length=6)),
                ('date_joined', models.DateTimeField()),
                ('is_maker', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MakerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pincode', models.CharField(max_length=6)),
                ('date_joined', models.DateTimeField()),
                ('is_maker', models.BooleanField(default=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
            bases=(models.Model,),
        ),
    ]
