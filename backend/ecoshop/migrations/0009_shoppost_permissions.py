# Generated by Django 3.1.7 on 2021-04-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0008_auto_20210421_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppost',
            name='permissions',
            field=models.BooleanField(default=False),
        ),
    ]
