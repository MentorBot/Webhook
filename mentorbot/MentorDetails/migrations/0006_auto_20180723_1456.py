# Generated by Django 2.0.2 on 2018-07-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MentorDetails', '0005_auto_20180723_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprofile',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='short_bio',
            field=models.TextField(),
        ),
    ]
