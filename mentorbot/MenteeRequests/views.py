from rest_framework import generics
from ..serializers import MentorDetailsSerializer, MentorshipFieldsSerializer, NewMentorshipFieldRequestSerializer, MenteeRequestNewMentorshipFieldSerializer
from .models import MentorDetails, MentorshipFields, MenteeRequestNewMentorshipField, NewMentorshipFieldRequest


class CreateView(generics.ListCreateAPIView):
    serializer_class = 
    pass
class ListView(generics.ListAPIView):
    serializer_class
    pass
class RetrieveView(generics.RetrieveAPIView):
    serializer_class
    pass
class DestroyView(generics.DestroyAPIView):
    serializer_class
    pass
class UpdateView(generics.UpdateAPIView):
    serializer_class = 
    pass
