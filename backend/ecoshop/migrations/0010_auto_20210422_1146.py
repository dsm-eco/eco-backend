# Generated by Django 3.1.7 on 2021-04-22 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0009_shoppost_permissions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppost',
            old_name='permissions',
            new_name='permission',
        ),
    ]
