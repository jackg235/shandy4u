# Generated by Django 2.2.7 on 2019-12-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerapp', '0002_drink_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='popular',
            field=models.IntegerField(default=0),
        ),
    ]