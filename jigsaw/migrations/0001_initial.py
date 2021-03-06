# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-11 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('pos_x', models.IntegerField()),
                ('pos_y', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='jigsaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('num_column', models.IntegerField()),
                ('num_row', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='from_jigsaw',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jigsaw.jigsaw'),
        ),
    ]
