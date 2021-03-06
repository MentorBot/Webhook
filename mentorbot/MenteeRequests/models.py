from django.db import models
from MentorDetails.models import MentorProfile

class MenteeRequests(models.Model):
    mentor = models.ForeignKey('MentorDetails.MentorUser', on_delete=models.CASCADE, related_name='requests', null=True)
    mentee_name = models.CharField(max_length=170, blank=False)
    email = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=150, default='Nairobi')
    bio = models.TextField(default='Mentor me please')
    request_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.email, self.mentee_name)

class NeedMentorRequests(models.Model):
    requester_email = models.EmailField(max_length=70, blank=False)
    requested_field = models.CharField(max_length=50, blank=False)
    request_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.requester_email, self.requested_field, self.request_status, self.date_created, self.date_modified
