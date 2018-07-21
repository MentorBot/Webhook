from rest_framework import generics
from rest_framework import filters
from mentorbot.serializers.mentorshipfieldserializer  import MentorshipFieldsSerializer
from .models import MentorshipFields


class CreateView(generics.ListCreateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

class ListView(generics.ListAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('field_name')


class RetrieveView(generics.RetrieveAPIView):
    print('------- tumefika mentorshipfields retrieve!!')
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     obj = queryset.get(field_name=self.request.MentorshipFields.field_name)
    #     return obj

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

class DestroyView(generics.DestroyAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
