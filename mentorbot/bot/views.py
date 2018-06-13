# from rest_framework import generics
from django.views import generic
from django.shortcuts import render
from django.http.response import HttpResponse
import json, requests, random, re
from decouple import config
from simple_search import search_filter
from .models import Bot
from MentorshipFields.models import MentorshipFields

PAGE_ACCESS_TOKEN=config('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN= config('VERIFY_TOKEN')

class FacebookMessengerWebhook(generic.View):
    def get(self, request):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

class SlackWebhook(generic.View):
    print("This is Slack Webhook")

class TwitterWebhook(generic.View):
    print("This is Twitter Webhook")

class ChatBotResponse(generic.View):
    print("This are chatbot responses")

class error_404_view(generic.View):
    def get(self, request):
        data = {"name": "MentorMe.com"}
        return render (request,'/error_404.html', data)
