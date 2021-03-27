# Generated by Django 3.1.7 on 2021-03-25 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0012_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bPic', models.ImageField(default='defaultproban.jpg', upload_to='project_banner')),
                ('logo', models.ImageField(default='defaultlogo.jpg', upload_to='project_logo')),
                ('department', models.CharField(choices=[('Behavioral Sciences and Leadership', 'Behavioral Sciences and Leadership'), ('Chemistry and Life Science', 'Chemistry and Life Science'), ('Civil and Mechanical Engineering', 'Civil and Mechanical Engineering'), ('Electrical Engineering and Comptuer Science', 'Electrical Engineering and Comptuer Science'), ('English and Philosophy', 'English and Philosophy'), ('Foreign Languages', 'Foreign Languages'), ('Geography and Environmental Engineering', 'Geography and Environmental Engineering'), ('History', 'History'), ('Law', 'Law'), ('Mathematical Sciences', 'Mathematical Sciences'), ('Physics and Nuclear Engineering', 'Physics and Nuclear Engineering'), ('Social Sciences', 'Social Sciences'), ('Systems Engineering', 'Systems Engineering'), ('Independent', 'Independent')], default='Independent', max_length=50)),
                ('description', models.CharField(max_length=50, null=True)),
                ('purpose', models.TextField()),
                ('projectTag', models.CharField(choices=[('Data Analysis', 'Data Analysis'), ('3D Printing', '3D Printing'), ('Robotics', 'Robotics'), ('Coding', 'Coding'), ('Aerodynamics', 'Aerodynamics')], default='Coding', max_length=32)),
                ('lookingFor', models.CharField(choices=[('motivated cadets with niche expertise.', 'Expert Cadets'), ('cadets who want to learn and help.', 'Any cadet who wants to help'), ('an engineering cadet.', 'Engineering Cadet'), ('a cadet with a scientific background.', 'Scientific background'), ('cadets with programming experience.', 'Coding Background')], default='an engineering cadet,', max_length=75)),
                ('recruiting', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=50)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Archived', 'Archived'), ('Deleted', 'Deleted')], default='Active', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'teams',
            },
        ),
        migrations.CreateModel(
            name='userTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='projectTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
        migrations.CreateModel(
            name='departmentTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]