from django.contrib import admin
from .models import Bot, Profile

MOdeLS = [Bot, Profile]
for model in MOdeLS:
    admin.site.register(model)
