# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-10 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apostello', '0003_delete_elvantogroup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DefaultResponses',
        ),
        migrations.DeleteModel(
            name='SiteConfiguration',
        ),
    ]
