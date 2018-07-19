from django.db import models

class MentorshipFields(models.Model):
    field_name = models.CharField(max_length=20, unique=True)
    field_details = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ('field_name',)

    def __str__(self):
        return self.field_name, self.field_details
