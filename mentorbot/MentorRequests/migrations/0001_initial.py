# Generated by Django 2.0.1 on 2018-01-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MentorRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_name', models.CharField(max_length=50)),
                ('mentor_approved', models.CharField(max_length=50)),
                ('requested_mentorship_field', models.CharField(max_length=50)),
                ('request_status', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
