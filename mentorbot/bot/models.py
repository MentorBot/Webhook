from django.db import models

class Bot(models.Model):
    field_name = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.field_name, self.date_created