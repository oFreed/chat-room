# Generated by Django 3.1.7 on 2021-04-08 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210408_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('text', models.TextField(max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 4, 8, 18, 2, 23, 934721), verbose_name='create date')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='update date')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
