
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializer import MentorDetailsSerializer
from .models import MentorDetails
from rest_framework import generics


class CreateView(generics.CreateAPIView):
    '''creates the user'''
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()


class ListView(generics.ListAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer


class RetrieveView(generics.RetrieveAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer


class DestroyView(generics.DestroyAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer


class UpdateView(generics.UpdateAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer
