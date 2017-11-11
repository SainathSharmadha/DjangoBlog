# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171111_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_comments',
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='user',
            field=models.TextField(null=True),
        ),
    ]
