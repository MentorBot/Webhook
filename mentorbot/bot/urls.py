
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url, include, handler404
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FacebookMessengerWebhook, SlackWebhook, TwitterWebhook, ChatBotResponse, error_404_view

from django.views.generic import TemplateView

from .views import CreateView, ListView, RetrieveView, SearchListView
from . import main


urlpatterns = {
    url('^$', TemplateView.as_view(template_name='index.html')),
    url(r'^bot_add$', CreateView.as_view(), name="create"),
    url(r'^bot_search$', SearchListView.as_view(), name="search"),
    url(r'^bot_list$', ListView.as_view(), name="list"),
    url(r'^bot_list0$', RetrieveView.as_view(), name="retrieve"),
    url(r'^index$', main.index, name='index'),
    url(r'^become_mentor$', main.become_mentor, name='become_mentor'),
    url(r'^find_mentor$', main.find_mentor, name='find_mentor'),

    url(r'^messenger_webhook/?$', FacebookMessengerWebhook.as_view(), name="Facebook Messenger Webhook"),
    url(r'^slack_webhook$', SlackWebhook.as_view(), name="Slack Webhook"),
    url(r'^twitter_webhook$', TwitterWebhook.as_view(), name="Twitter Webhook"),
    url(r'^chatbot_responses$', ChatBotResponse.as_view(), name="ChatBot Response"),

}
urlpatterns = format_suffix_patterns(urlpatterns)

handler404 = 'views.error_404_view'
