from rest_framework import generics
from mentorbot.serializers.mentorrequestsserializer  import MentorRequestsSerializer
from .models import MentorRequests


class CreateView(generics.ListCreateAPIView):
    queryset = MentorRequests.objects.all()
    serializer_class = MentorRequestsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()

class ListView(generics.ListAPIView):
    queryset = MentorRequests.objects.all()
    serializer_class = MentorRequestsSerializer

class RetrieveView(generics.RetrieveAPIView):
    queryset = MentorRequests.objects.all()
    serializer_class = MentorRequestsSerializer

class DestroyView(generics.DestroyAPIView):
    queryset = MentorRequests.objects.all()
    serializer_class = MentorRequestsSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = MentorRequests.objects.all()
    serializer_class = MentorRequestsSerializer
