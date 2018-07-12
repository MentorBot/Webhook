from rest_framework import generics
<<<<<<< HEAD
from mentorbot.serializers.mentorshipfieldserializer  import MentorshipFieldsSerializer
=======
from mentorbot.serializers import MentorshipFieldsSerializer
>>>>>>> implement mentor functionality.
from .models import MentorshipFields


class CreateView(generics.ListCreateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Mentee Request."""
        serializer.save()

<<<<<<< HEAD
=======

>>>>>>> implement mentor functionality.
class ListView(generics.ListAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

<<<<<<< HEAD
=======

>>>>>>> implement mentor functionality.
class RetrieveView(generics.RetrieveAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

<<<<<<< HEAD
=======

>>>>>>> implement mentor functionality.
class DestroyView(generics.DestroyAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer

<<<<<<< HEAD
=======

>>>>>>> implement mentor functionality.
class UpdateView(generics.UpdateAPIView):
    queryset = MentorshipFields.objects.all()
    serializer_class = MentorshipFieldsSerializer
