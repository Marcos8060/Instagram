# Generated by Django 4.0.3 on 2022-04-08 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
