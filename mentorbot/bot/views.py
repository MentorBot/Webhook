from rest_framework import generics
from mentorbot.serializers import BotSerializer
from mentorbot.serializers import MentorshipFieldsSerializer
from django.views import generic
from django.shortcuts import render
from django.http.response import HttpResponse
from slackclient import SlackClient
import json, requests, random, re
from decouple import config

from simple_search import search_filter
from .models import Bot
from MentorshipFields.models import MentorshipFields

PAGE_ACCESS_TOKEN=config('PAGE_ACCESS_TOKEN')
VERIFY_TOKEN= config('VERIFY_TOKEN')
slack_client = SlackClient(config('SlackClient'))

class FacebookMessengerWebhook(generic.View):
    '''returns responses to facebook messenger bot'''
    def get(self, request):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    def post(self, request, *args, **kwargs):
        pass

    def format_response(self, message):
        pass

class SlackWebhook(generic.View):
    '''returns responses to slack bot'''
    def get(self, request):
        return HttpResponse('This is Slack Webhook')

    def post(self, request, *args, **kwargs):
        pass

    def format_response(self, message):
        pass


class TwitterWebhook(generic.View):
    '''returns responses to twitter bot'''
    def get(self, request):
        return HttpResponse('This is twitter Webhook')

    def post(self, request, *args, **kwargs):
        pass

    def format_response(self, message):
        pass


class ChatBotResponse(generic.View):
    '''returns the required response to the right bot'''
    print("This are chatbot responses")

def check_incoming_bot(self, message):
    '''this checks the message coming in and determines the bot that is trying to get a response based on the content of the message'''
    pass
