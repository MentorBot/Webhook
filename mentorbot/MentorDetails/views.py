from rest_framework import generics
from django.http.response import HttpResponse
from mentorbot.serializers  import MentorDetailsSerializer, MentorLoginSerializer
from .models import MentorDetails, MentorLogin

class MentorDetailsCreateView(generics.ListCreateAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer

    def create(self, serializer):
        """Save the post data when creating a new Mentor."""
        serializer.save()


class MentorDetailsListView(generics.ListAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer

    def get(self, request):
        return HttpResponse('create')

class MentorDetailsRetrieveView(generics.RetrieveAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer

    def retrieve(self, request):
        return HttpResponse('retrieve')

class MentorDetailsDestroyView(generics.DestroyAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer

    def delete(self, request):
        return HttpResponse('delete')

class MentorDetailsUpdateView(generics.UpdateAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer

    def update(self, request):
        return HttpResponse('update')

class MentorList(generics.ListCreateAPIView):
    queryset = MentorLogin.objects.all()
    serilaizer_class = MentorLoginSerializer

class MentorLoginDetails(generics.RetrieveUpdateDestroyAPIView):
    serilaizer_class = MentorLoginSerializer

    def get(self):
        return MentorLogin.objects.all().filter(username=self.request.username)
