from django.db import models

class MenteeRequests(models.Model):
    mentee_name = models.CharField(max_length=50)
    requested_mentorship_field = models.CharField(max_length=50)
    request_status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.mentee_name, self.requested_mentorship_field, self.request_status, self.date_created, self.date_modified
