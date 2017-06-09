# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-28 14:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myAnalyzer', '0008_auto_20161226_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appinventorLogin', models.TextField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='projectProperties',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]