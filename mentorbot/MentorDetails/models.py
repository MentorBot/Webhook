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
    REQUIRED_FIELDS = ['email']

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
    user = models.OneToOneField(MentorUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, unique=True)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    linkdin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image')
    location = models.CharField(max_length=30, blank=True)
    short_bio = models.TextField()
    mentor_status = models.BooleanField(default=False)
    mentorship_field = models.CharField(max_length=100)
    mentorship_details = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    mentoraccount = models.ForeignKey('MentorLogin.username', related_name='menotrdetails', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering=('date_created',)

    def __str__(self):
        return self.name, self.phone_nummber, self.email, self.linkdin, self.github, self.facebook, self.twitter, self.location, self.mentorship_field, self.mentorship_detials, self.date_created, self.date_modified

@receiver(post_save, sender=MentorUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        MentorProfile.objects.create(user=instance)

@receiver(post_save, sender=MentorUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
