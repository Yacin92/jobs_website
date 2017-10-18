# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 14:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_search', '0004_auto_20170402_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='region',
            field=models.CharField(choices=[('sfax', 'sfax'), ('monastir', 'monastir')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='annonce',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]