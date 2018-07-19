from rest_framework import generics
from mentorbot.serializers.mentorshipfieldserializer  import MentorshipFieldsSerializer
from .models import MentorshipFields


class CreateView(generics.ListCreateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

class ListView(generics.ListAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer


class RetrieveView(generics.RetrieveAPIView):
    lookup_field = 'field_name'
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

class DestroyView(generics.DestroyAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
