from rest_framework import generics
from method_decorator import method_decorator
from django.views.decorators.csrf import csrf_exempt
from mentorbot.serializers.botserializer import BotSerializer
from mentorbot.serializers.mentorshipfieldserializer import MentorshipFieldsSerializer
from django.views import generic
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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        v = ChatBotResponse()
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    print(message)
                    v.post_facebook_message(message['sender']['id'], message['message']['text'])

        return HttpResponse()

    def format_response(self, message):
        return("-----", message)

class SlackWebhook(generic.View):
    '''returns responses to slack bot'''
    def get(self, request):
        return HttpResponse('This is Slack Webhook')

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is Slack Webhook')

    def format_response(self, message):
        return("-----", message)


class TwitterWebhook(generic.View):
    '''returns responses to twitter bot'''
    def get(self, request):
        return HttpResponse('This is twitter Webhook')

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is twitter Webhook')

    def format_response(self, message):
        return("-----", message)


class ChatBotResponse(generic.View):
    '''returns the required response to the right bot'''
    def post_facebook_message(self, fbid, recevied_message):
        params = {
        "page_access_token": "PAGE_ACCESS_TOKEN"
        }
        headers = {
        "Content-Type": "application/json"
        }
        data = json.dumps({
        "recipient": {
            "id": fbid
        },
        "message": {
            "text": recevied_message
        }
        })
        r = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=", params=params, headers=headers, data=data)
        if r.status_code != 200:
            print(r.status_code)
            print(r.text)
