# Generated by Django 2.0.2 on 2018-07-23 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MentorDetails', '0008_mentorprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MentorDetails.MentorUser'),
        ),
    ]
