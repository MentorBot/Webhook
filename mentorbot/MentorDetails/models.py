from django.db import models
from django.core.mail import EmailMessage
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _

from mentorbot.usermanager import UserManager


class MentorDetails(AbstractUser):
    username = models.CharField(_('username'), max_length=30, blank=True)
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('first_name'), max_length=30, blank=True)
    last_name = models.CharField(_('last_name'), max_length=30, blank=True)
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(default='pic02.jpg',
                               upload_to='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

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
        email = EmailMessage(subject, message, to=[self.email])
        email.send()

    def __str__(self):
        return "{0}, {1}".format(self.name, self.email)
