from rest_framework import generics
from ..serializers import MenteeRequestsSerializer
from .models import  MenteeRequests

class CreateView(generics.ListCreateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()

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
