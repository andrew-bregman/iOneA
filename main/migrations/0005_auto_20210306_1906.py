# Generated by Django 3.1.7 on 2021-03-07 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210306_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ubio',
            old_name='department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='ubio',
            old_name='major',
            new_name='Major',
        ),
        migrations.RenameField(
            model_name='ubio',
            old_name='meetMe',
            new_name='MeetMe',
        ),
        migrations.RenameField(
            model_name='ubio',
            old_name='minor',
            new_name='Minor',
        ),
        migrations.RenameField(
            model_name='ubio',
            old_name='title',
            new_name='Title',
        ),
    ]