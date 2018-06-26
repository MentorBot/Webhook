from rest_framework import generics
from django.http.response import HttpResponse
from mentorbot.serializers.mentordetailsserializers  import MentorProfileSerializer, MentorUserSerializer
from .models import MentorProfile, MentorUser

class MentorDetailsCreateView(generics.ListCreateAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def create(self, serializer):
        """Save the post data when creating a new Mentor."""
        serializer.save()


class MentorDetailsListView(generics.ListAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def get(self, request):
        return HttpResponse('create')

class MentorDetailsRetrieveView(generics.RetrieveAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def retrieve(self, request):
        return HttpResponse('retrieve')

class MentorDetailsDestroyView(generics.DestroyAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def delete(self, request):
        return HttpResponse('delete')

class MentorDetailsUpdateView(generics.UpdateAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def update(self, request):
        return HttpResponse('update')

class MentorList(generics.ListCreateAPIView):
    queryset = MentorUser.objects.all()
    serilaizer_class = MentorUserSerializer

class MentorLoginDetails(generics.RetrieveUpdateDestroyAPIView):
    serilaizer_class = MentorUserSerializer

    def get(self):
        return MentorUser.objects.all().filter(email=self.request.email)
