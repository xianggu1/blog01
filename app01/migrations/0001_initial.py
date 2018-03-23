# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=70)),
                ('body', models.TextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], verbose_name='文章状态', max_length=1)),
                ('abstract', models.CharField(blank=True, verbose_name='摘要', null=True, help_text='可选，如若为空将摘取正文的前54个字符', max_length=54)),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('topped', models.BooleanField(default=False, verbose_name='置顶')),
            ],
            options={
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='类名', max_length=20)),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.Category', verbose_name='分类'),
        ),
    ]
