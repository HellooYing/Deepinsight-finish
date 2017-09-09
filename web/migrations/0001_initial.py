# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 10:41
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='邮箱/电话号码')),
                ('name', models.CharField(max_length=50, verbose_name='真实姓名')),
                ('unit', models.CharField(max_length=30, verbose_name='单位')),
                ('office', models.CharField(max_length=50, verbose_name='科室')),
                ('post', models.CharField(max_length=50, verbose_name='职务')),
                ('professional', models.CharField(max_length=50, verbose_name='职称')),
                ('number', models.CharField(max_length=50, verbose_name='工号')),
                ('isadmin', models.BooleanField(default=False, verbose_name='是否为管理员')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_time', models.DateTimeField(auto_now=True, max_length=50, verbose_name='申请日期')),
                ('ratify_time', models.DateTimeField(auto_now=True, max_length=50, verbose_name='批准日期')),
                ('limit_time', models.DateTimeField(max_length=50, verbose_name='有效时间')),
                ('activation', models.CharField(default='待发放', max_length=50, verbose_name='激活码')),
                ('SNnum', models.CharField(default='待发放', max_length=50, verbose_name='SN号')),
                ('examine', models.CharField(default='未审核', max_length=50, verbose_name='审核')),
                ('pass_or_not', models.NullBooleanField(default='', verbose_name='是否通过')),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='', verbose_name='个人')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
