# Generated by Django 2.1.7 on 2019-03-29 03:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190328_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 29, 3, 59, 18, 563923, tzinfo=utc)),
        ),
    ]
