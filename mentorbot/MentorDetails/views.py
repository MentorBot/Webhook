
from rest_framework import generics, authentication, permissions
from rest_framework.views import APIView
from django.http.response import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework.authtoken.models import Token
from mentorbot.serializers.mentordetailsserializers  import MentorProfileSerializer, MentorUserSerializer
from .models import MentorProfile, MentorUser
from rest_framework import generics


class MentorDetailsCreateUser(generics.CreateAPIView):
    '''creates the user'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorUserSerializer

    def post(self, request, format='json'):
        """Save the post data when creating a new Mentor."""
        print("-----------------tumefika register")
        data=request.data
        serializer = MentorUserSerializer()
        if serializer.is_valid():
            user = serializer.create(data)
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

    # def get(self, request, format=None):
    #     email = [user.email for user in MentorUser.objects.all()]
    #     return HttpResponse('Welcome to Mentor Bot Register Endpoint', email)


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

class LoginView(APIView):
    def post(self, request, format=None):
        pass

class LogoutView(APIView):
    def post(self, request, format=None):
        pass
