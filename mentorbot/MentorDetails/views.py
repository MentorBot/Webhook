from rest_framework import generics
from mentorbot.serializers import MentorDetailsSerializer
from .models import MentorDetails


class CreateView(generics.ListCreateAPIView):
    queryset = MentorDetails.objects.all()
    serializer_class = MentorDetailsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Mentor."""
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
