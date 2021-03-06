# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-18 16:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referrals', '0002_auto_20180130_0904'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='День платежа')),
                ('paid', models.BooleanField(default=False, verbose_name='Статус оплаты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор платежа')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежы',
                'db_table': 'payment',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='Накопленные бонусы за предыдущие месяцы')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('address', models.CharField(max_length=500, verbose_name='Адрес проживания')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Номер телефона')),
                ('first_name', models.CharField(max_length=250, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=250, verbose_name='Отчетство')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dashboard.Profile', verbose_name='Родитель пользователя')),
                ('referral', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='referrals.Referral', verbose_name='Реферал')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
                'db_table': 'profile',
            },
        ),
    ]
