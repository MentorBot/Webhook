from django.db import models

class MentorDetails(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    phone_nummber = models.IntegerField()
    email = models.CharField(max_length=100)
    linkdin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    mentor_status = models.BooleanField(default=False)
    mentorship_field = models.CharField(max_length=100)
    mentorship_detials = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name, self.phone_nummber, self.email, self.linkdin, self.github, self.facebook, self.twitter, self.mentorship_field, self.mentorship_detials, self.date_created, self.date_modified

class MentorshipFields(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class NewMentorshipFieldRequest(models.Model):
    requester_name = models.CharField(max_length=50)
    requester_approved = models.CharField(max_length=50)
    requested_mentorship_field = models.CharField(max_length=50)
    request_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.requester_name, self.requester_approved, self.requested_mentorship_field, self.request_status, self.date_created, self.date_modified

class MenteeRequestNewMentorshipField(models.Model):
    mentee_name = models.CharField(max_length=50)
    requested_mentorship_field = models.CharField(max_length=50)
    request_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return self.mentee_name, self.requested_mentorship_field, self.request_status, self.date_created, self.date_modified
