# Generated by Django 2.0.2 on 2018-03-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20180306_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
