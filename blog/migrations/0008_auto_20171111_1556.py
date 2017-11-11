# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171111_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='user',
            field=models.CharField(null=True, max_length=200),
        ),
    ]
