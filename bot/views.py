from rest_framework import generics
from mentorbot.serializers  import BotSerializer
from .models import Bot


class CreateView(generics.ListCreateAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()
    
class ListView(generics.ListAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    
class RetrieveView(generics.RetrieveAPIView):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    
