# Generated by Django 3.1.7 on 2021-03-08 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210307_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Faculty', 'Faculty'), ('Cadet', 'Cadet')], default='Cadet', max_length=50),
        ),
    ]
