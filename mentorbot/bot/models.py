from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from MentorDetails.models import MentorDetails


class Bot(models.Model):
    field_name = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field_name, self.date_created


class Profile(models.Model):
    user = models.OneToOneField(MentorDetails, on_delete=models.CASCADE,
                                related_name='profile')
    email_confirmed = models.BooleanField(default=False)

    @receiver(post_save, sender=MentorDetails)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
