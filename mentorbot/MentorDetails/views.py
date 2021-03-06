
from rest_framework import generics, authentication, permissions
from rest_framework import status
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from mentorbot.serializers.mentordetailsserializers  import MentorProfileSerializer, MentorUserSerializer, TokenSerializer
from .models import MentorProfile, MentorUser
from mentorbot.settings import base
from rest_framework import generics
from rest_framework import filters


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class MentorDetailsCreateUser(generics.CreateAPIView):
    '''creates the user'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not password and not email:
            return HttpResponse(
                "password and email is required to register a user",
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            MentorUser.objects.create_user(password=password, email=email)
            return HttpResponse("User created succesfully",
                status=status.HTTP_201_CREATED)

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
    permission_classes = (permissions.IsAuthenticated,)

class MentorDestroyUserNoProfile(generics.DestroyAPIView):
    '''Deletes User when profile has not been saved succesfully'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorProfileSerializer

class MentorDetailsDestroyUser(generics.DestroyAPIView):
    '''Deletes User'''
    queryset = MentorUser.objects.all()
    serializer_class = MentorProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

"""|------------------------------------------------------|"""

# class MentorProfileCreate(generics.CreateAPIView):
#     queryset = MentorProfile.objects.all()
#     serializer_class = MentorProfileSerializer




class MentorProfileListUsers(generics.ListAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

class MentorProfileListUser(generics.ListAPIView):
    '''returns one profile'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

class FieldListView(generics.ListAPIView):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('field_name')

class MentorProfileUpdate(generics.UpdateAPIView):
    '''update one profile'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

class MentorProfileDestroy(generics.DestroyAPIView):
    '''destroy one profile'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

"""----------------------------------------------------------"""

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = MentorUser.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return HttpResponse(serializer.data, status.HTTP_200_OK)
        return HttpResponse(data={
            "message": "User does not exist, please enter your credentials again"
        }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(generics.CreateAPIView):
    queryset = MentorUser.objects.all()

    def get(self, request, format=None):
        request.MentorUser.auth_token.delete()
        return HttpResponse(status=status.HTTP_200_OK)
