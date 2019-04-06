# Generated by Django 2.1.7 on 2019-03-28 16:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(upload_to='')),
                ('adress', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=100)),
                ('advertisement', models.TextField()),
                ('published_date', models.DateTimeField(default=datetime.datetime(2019, 3, 28, 16, 25, 1, 561729, tzinfo=utc))),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Companies')),
            ],
        ),
    ]
