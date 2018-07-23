# Generated by Django 2.0.2 on 2018-07-23 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MentorDetails', '0004_auto_20180721_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentoruser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='mentoruser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='mentoruser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='mentoruser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='mentoruser',
            name='username',
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='image',
            field=models.FileField(default='pic05.jpg', upload_to='.../templtes/images/profile_pictures'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MentorDetails.MentorUser'),
        ),
        migrations.AlterField(
            model_name='mentoruser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentoruser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]