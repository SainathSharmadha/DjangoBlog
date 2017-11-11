# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='/images/pic1.jpeg', upload_to=''),
        ),
    ]
