# Generated by Django 3.2.13 on 2022-05-31 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='boby',
            new_name='body',
        ),
    ]
