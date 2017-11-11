# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171111_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_comments',
            field=models.ManyToManyField(to='blog.UserComment'),
        ),
    ]
