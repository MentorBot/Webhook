from django.conf.urls import url, include, handler404
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FacebookMessengerWebhook, SlackWebhook, TwitterWebhook, ChatBotResponse, error_404_view
from django.views.generic import TemplateView
from .admin import admin

urlpatterns = {
    url('^$', TemplateView.as_view(template_name='index.html')),
    url(r'^messenger_webhook', FacebookMessengerWebhook.as_view(), name="Facebook Messenger Webhook"),
    url(r'^slack_webhook$', SlackWebhook.as_view(), name="Slack Webhook"),
    url(r'^twitter_webhook$', TwitterWebhook.as_view(), name="Twitter Webhook"),
    url(r'^chatbot_responses$', ChatBotResponse.as_view(), name="ChatBot Response"),
}
urlpatterns = format_suffix_patterns(urlpatterns)

handler404 = 'views.error_404_view'
