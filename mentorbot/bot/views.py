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


from mentorbot.serializers import BotSerializer
from mentorbot.serializers import MentorshipFieldsSerializer

from simple_search import search_filter
from .models import Bot
from .chatresponsehandler import Response
from MentorshipFields.models import MentorshipFields

VERIFY_TOKEN= config('VERIFY_TOKEN')
slack_client = SlackClient(config('SlackClient'))


def post_facebook_message(fbid, recevied_message):
    '''returns the required response to the right bot'''
    PAGE_ACCESS_TOKEN=config('PAGE_ACCESS_TOKEN')
    RESPONSE = Response(fbid, recevied_message)

    params = {
    'access_token': PAGE_ACCESS_TOKEN
    }
    headers = {
    'Content-Type': 'application/json'
    }
    data = json.dumps(RESPONSE)

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
        return

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
                    print("------------- message", type(message))
                    print(message['sender']['id'])
                    print(message['message']['text'])
                    post_facebook_message(message['sender']['id'], message['message']['text'])

        return HttpResponse()

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

class CreateView(generics.ListCreateAPIView):
    """When a user searches for  a mentorship field,\
     the field is recorded in the bot db"""
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a bot search."""
        serializer.save()


class ListView(generics.ListAPIView):
    """This lists all the mentorship requests made"""
    queryset = Bot.objects.all()
    serializer_class = BotSerializer


class SearchListView(generics.ListAPIView):
    """ this allows users to make queries such as\
     http://example.com/bot/search?name=python"""
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
    filter_fields = ('^name')


class RetrieveView(generics.RetrieveAPIView):
    """This should display one bot request"""
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

