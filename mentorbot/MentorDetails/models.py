from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from mentorbot.usermanager import UserManager


class MentorUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    last_login = models.CharField(max_length=250, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return '{}'.format(self.email)

    class Meta:
        verbose_name = _('mentoruser')
        verbose_name_plural = _('mentorusers')


class MentorProfile(models.Model):
    user = models.OneToOneField('MentorUser', on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    linkdin = models.CharField(max_length=100)


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
    image = models.ImageField(upload_to='bot/static/images')
    short_bio = models.TextField()
    mentor_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{0}, {1}".format(self.name, self.email)
