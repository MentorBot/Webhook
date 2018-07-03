from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from mentorbot.serializers.mentordetailsserializers  import MentorProfileSerializer, MentorUserSerializer
from .models import MentorProfile, MentorUser


class MentorDetailsCreateUsers(generics.CreateAPIView):
    '''creates the user'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorUserSerializer

    def post(self, request, format='json'):
        """Save the post data when creating a new Mentor."""
        serializer = MentorUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)

        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MentorDetailsListUsers(generics.ListAPIView):
    """Return a list of all users."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    queryset = MentorUser.objects.all()
    serializer_class = MentorUserSerializer

    def get(self, request, format=None):
        email = [user.email for user in MentorUser.objects.all()]
        return HttpResponse('Welcome to Mentor Bot Register Endpoint', email)


class MentorDetailsListUser(generics.ListAPIView):
    """Return a list of one users."""
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def get(self, request):
        return HttpResponse('create')

class MentorDetailsRetrieveView(generics.RetrieveAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def retrieve(self, request):
        return HttpResponse('retrieve')

# class MentorDetailsDestroyView(generics.DestroyAPIView):
#     queryset = MentorProfile.objects.all()
#     serializer_class = MentorProfileSerializer

#     def delete(self, request):
#         return HttpResponse('delete')

# class MentorDetailsUpdateView(generics.UpdateAPIView):
#     queryset = MentorProfile.objects.all()
#     serializer_class = MentorProfileSerializer

#     def update(self, request):
#         return HttpResponse('update')

class MentorProfileView(generics.ListAPIView):
    queryset = MentorUser.objects.all()
    serilaizer_class = MentorUserSerializer

class MentorLoginDetails(generics.RetrieveUpdateDestroyAPIView):
    serilaizer_class = MentorUserSerializer

    def get(self):
        return MentorUser.objects.all().filter(email=self.request.email)

class LoginView(APIView):
    def post(self, request, format=None):
        pass

class LogoutView(APIView):
    def post(self, request, format=None):
        pass
