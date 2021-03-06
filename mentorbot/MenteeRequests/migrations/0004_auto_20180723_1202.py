# Generated by Django 2.0.2 on 2018-07-23 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MenteeRequests', '0003_auto_20180723_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menteerequests',
            name='bio',
            field=models.TextField(default='Mentor me please', max_length=200),
        ),
        migrations.AlterField(
            model_name='menteerequests',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='menteerequests',
            name='mentee_name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='menteerequests',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='MentorDetails.MentorProfile'),
        ),
    ]
