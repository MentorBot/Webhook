from rest_framework import generics
from django.http.response import HttpResponse
from mentorbot.serializers  import MenteeRequestsSerializer
from .models import  MenteeRequests

class CreateView(generics.ListCreateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

    def create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()

class ListView(generics.ListAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

    def get(self, requests):
        return HttpResponse('get')

class RetrieveView(generics.RetrieveAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

class DestroyView(generics.DestroyAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer
