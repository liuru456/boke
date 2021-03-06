# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-12 08:24
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '类别'},
        ),
        migrations.AlterModelOptions(
            name='blogapp',
            options={'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='category',
            name='cname',
            field=models.CharField(max_length=30, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='blogapp',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Category', verbose_name='所属类别'),
        ),
        migrations.AlterField(
            model_name='blogapp',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blogapp',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='blogapp',
            name='tag',
            field=models.ManyToManyField(to='blogapp.Tag', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='blogapp',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tname',
            field=models.CharField(max_length=30, verbose_name='标签'),
        ),
    ]
