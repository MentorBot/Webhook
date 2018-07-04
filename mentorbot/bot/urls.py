from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FacebookMessengerWebhook, SlackWebhook, TwitterWebhook


urlpatterns = {
    url(r'^messenger_webhook/?$', FacebookMessengerWebhook.as_view(), name="Facebook Messenger Webhook"),
    url(r'^slack_webhook$', SlackWebhook.as_view(), name="Slack Webhook"),
    url(r'^twitter_webhook$', TwitterWebhook.as_view(), name="Twitter Webhook")

}
urlpatterns = format_suffix_patterns(urlpatterns)
