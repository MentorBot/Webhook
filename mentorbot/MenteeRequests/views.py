from rest_framework import generics
from django.http.response import HttpResponse
from mentorbot.serializers.menteerequestserializer import MenteeRequestsSerializer
from .models import MenteeRequests


class CreateView(generics.ListCreateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

class ListView(generics.ListAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer


class RetrieveView(generics.RetrieveAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer


class DestroyView(generics.DestroyAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer



class UpdateView(generics.UpdateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer


"""----------------------------------"""

class NeedMentor(generics.ListCreateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer
