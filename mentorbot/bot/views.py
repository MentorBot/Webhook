from rest_framework import generics
from mentorbot.serializers import BotSerializer
from mentorbot.serializers import MentorshipFieldsSerializer
from simple_search import search_filter
from .models import Bot
from MentorshipFields.models import MentorshipFields


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
