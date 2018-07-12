from rest_framework import generics
<<<<<<< HEAD
from django.http.response import HttpResponse
from mentorbot.serializers.menteerequestserializer  import MenteeRequestsSerializer
from .models import  MenteeRequests
=======
from mentorbot.serializers import MenteeRequestsSerializer
from .models import MenteeRequests

>>>>>>> implement mentor functionality.

class CreateView(generics.ListCreateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

    def create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()


class ListView(generics.ListAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

<<<<<<< HEAD
    def get(self, requests):
        return HttpResponse('get')
=======
>>>>>>> implement mentor functionality.

class RetrieveView(generics.RetrieveAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer
    def retrieve(self, requests):
        return HttpResponse('retrieve')


class DestroyView(generics.DestroyAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

<<<<<<< HEAD
    def delete(self, requests):
        return HttpResponse('delete')
=======
>>>>>>> implement mentor functionality.

class UpdateView(generics.UpdateAPIView):
    queryset = MenteeRequests.objects.all()
    serializer_class = MenteeRequestsSerializer

    def update(self, requests):
        return HttpResponse('update')
