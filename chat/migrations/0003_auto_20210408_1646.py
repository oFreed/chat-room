# Generated by Django 3.1.7 on 2021-04-08 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210408_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 16, 46, 55, 633300), verbose_name='create date'),
        ),
    ]
