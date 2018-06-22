from django.db import models


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
