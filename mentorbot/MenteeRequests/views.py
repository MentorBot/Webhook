from rest_framework import generics, permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import parser_classes
from django.http.response import HttpResponse
from mentorbot.serializers.menteerequestserializer import MenteeRequestsSerializer, NeedMentorRequestsSerializer
from .models import MenteeRequests, NeedMentorRequests


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
    queryset = NeedMentorRequests.objects.all()
    serializer_class = NeedMentorRequestsSerializer
    parser_classes = (FormParser,MultiPartParser, )
    permission_classes = (permissions.AllowAny,)
