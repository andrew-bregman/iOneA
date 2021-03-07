# Generated by Django 3.1.7 on 2021-03-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210306_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='CIC_OIC',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Purpose',
        ),
        migrations.RemoveField(
            model_name='project',
            name='currentlyWorkingOn',
        ),
        migrations.RemoveField(
            model_name='project',
            name='ifRecruting',
        ),
        migrations.RemoveField(
            model_name='project',
            name='numUsers',
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
