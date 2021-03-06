# Generated by Django 2.0.2 on 2018-07-24 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MentorDetails', '0009_auto_20180723_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentorprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='mentorprofile',
            name='avatar',
            field=models.ImageField(default='pic.jpg', upload_to='.../templtes/images/profile_pictures'),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='MentorDetails.MentorUser'),
        ),
        migrations.AlterField(
            model_name='mentoruser',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
