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

# PAGE_ACCESS_TOKEN=config('PAGE_ACCESS_TOKEN')
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
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    print("------------- message", message)
                    post_facebook_message(message['sender']['id'], message['message']['text'])

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


def get_access_token():
    '''get valid token from facebook'''
    app_id = config('APP_ID')
    app_secret = config('APP_SECRET')
    client_credentials = config('client_credentials')
    r = requests.post("https://graph.facebook.com/oauth/access_token?", client_id=app_id, client_secret=app_secret, grant_type=client_credentials)
    print('------r', r)
    return r



def post_facebook_message(fbid, recevied_message):
    '''returns the required response to the right bot'''
    get_access_token()
    params = {
    'access_token': 'EAACEdEose0cBAI98m0szWZBXzLnoCYgVRRP1VIOZBSFl1pjtmn5tD722ZCXFz46GZA6uG1UiDW8RTaNpwsOmYNZAKoHNLUHamZCdYZBSc9Og7FyP9ocobpM8gNvyZAbxOkPZBdAZC2WZCVVuRmhZB7eWCnlXlYbTJ82GCpEnMFdLDrpZB841iENHlnNqYBgvbNjQROKIZD'
    }
    headers = {
    'Content-Type': 'application/json'
    }
    data = json.dumps({
        'messaging_type': 'RESPONSE',

        'recipient': {
            'id': fbid
            },
        'message': {
            'text': 'Hello World'
        }
    })
    print('-----params', params)
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
