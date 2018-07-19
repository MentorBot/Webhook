from django.db import models
from MentorDetails.models import MentorDetails


class MentorRequests(models.Model):
    mentor_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    short_bio = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}, {1}".format(self.mentee_name, self.email)
