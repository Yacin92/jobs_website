# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_search', '0003_auto_20170402_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='annonce',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs_search.User'),
        ),
    ]
