# Generated by Django 4.0 on 2022-03-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0002_alter_zone_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='times_reported',
            field=models.IntegerField(default=1),
        ),
    ]