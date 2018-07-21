from django.db import models

class MenteeRequests(models.Model):
    mentee_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=False)
    phone_number = models.IntegerField(blank=True)
    location = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    request_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.mentee_name, self.email, self.phone_number, self.bio, self.location, self.request_status, self.date_created, self.date_modified

class NeedMentorRequests(models.Model):
    requester_email = models.EmailField()
    requeted_field = models.CharField(max_length=50)
    request_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
           return self.requester_email, self.requeted_field, self.request_status, self.date_created, self.date_modified
