from rest_framework import generics
from mentorbot.serializers  import MenteeRequestsSerializer
from .models import MentorshipFields 


class CreateView(generics.ListCreateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()
        
class ListView(generics.ListAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
    
class RetrieveView(generics.RetrieveAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
    
class DestroyView(generics.DestroyAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
    
class UpdateView(generics.UpdateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
    
