from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from mentorbot.usermanager import UserManager


class MentorDetails(models.Model):
    name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkdin = models.CharField(max_length=100)
    mentorship_field = models.CharField(max_length=100)
    medium = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    image = models.ImageField(default='pic02.jpg', upload_to='bot/static/images/')
    short_bio = models.TextField()
    mentor_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    short_bio = models.TextField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.email)
