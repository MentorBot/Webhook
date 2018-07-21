
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from mentorbot.serializers.mentordetailsserializers  import MentorProfileSerializer, MentorUserSerializer
from .models import MentorProfile, MentorUser
from rest_framework import generics


class MentorDetailsCreateUser(generics.CreateAPIView):
    '''creates the user'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorUserSerializer()

class MentorDetailsListUsers(generics.ListAPIView):
    """Return a list of all users."""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)
    queryset = MentorUser.objects.all()
    serializer_class = MentorUserSerializer

class MentorDetailsListUser(generics.ListAPIView):
    """Return a list of one users."""
    queryset = MentorUser.objects.all()
    serializer_class = MentorProfileSerializer


class MentorDetailsUpdateUser(generics.UpdateAPIView):
    '''Updates user details'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorProfileSerializer


class MentorDetailsDestroyUser(generics.DestroyAPIView):
    '''Deletes User'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorProfileSerializer

"""|------------------------------------------------------|"""

class MentorProfileCreate(generics.CreateAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

class MentorProfileListUsers(generics.ListAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

class MentorProfileListUser(generics.ListAPIView):
    '''returns one profile'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

class MentorProfileUpdate(generics.UpdateAPIView):
    '''update one profile'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

class MentorProfileDestroy(generics.DestroyAPIView):
    '''destroy one profile'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

"""----------------------------------------------------------"""
