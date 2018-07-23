from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from mentorbot.usermanager import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class MentorUser(AbstractBaseUser):
    email = models.EmailField(_('email_address'), unique=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.CharField(max_length=250, null=True)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

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

    def __str__(self):
        return '{}'.format(self.email)

    class Meta:
        verbose_name = _('mentoruser')
        verbose_name_plural = _('mentorusers')


class MentorProfile(models.Model):
    user = models.OneToOneField('MentorUser', on_delete=models.CASCADE)
    first_name = models.CharField(_('first_name'), max_length=30, blank=False)
    last_name = models.CharField(_('last_name'), max_length=30, blank=False)
    phone_number = models.IntegerField(blank=True)
    linkdin = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    mentorship_field = models.CharField(max_length=100, blank=False)
    medium = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    image = models.FileField(default="pic05.jpg", upload_to= ".../templtes/images/profile_pictures")
    short_bio = models.TextField(blank=False)
    mentor_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @receiver(post_save, sender=MentorUser)
    def create_or_update_user_profile(self, sender, instance, created, **kwargs):
        if created:
            MentorProfile.objects.create(user=instance)
        instance.profile.save()

    class Meta:
        ordering=('date_created',)

    def __str__(self):
        return self.first_name, self.last_name, self.phone_nummber, self.linkdin, self.github, self.facebook, self.twitter, self.mentorship_field, self.image, self.date_created, self.date_modified
