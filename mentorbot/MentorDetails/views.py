
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
        print("-----------------tumefika")
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

class MentorDetailsUpdate(generics.UpdateAPIView):
    '''Updates user details'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def update(self, request):
        return HttpResponse('update')

class MentorDetailsDestroy(generics.DestroyAPIView):
    '''Deletes User'''
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

    def delete(self, request):
        return HttpResponse('delete')

class MentorProfileCreate(generics.CreateAPIView):
    queryset = MentorUser.objects.all()
    serilaizer_class = MentorUserSerializer

class MentorProfileListUsers(generics.ListAPIView):
    serilaizer_class = MentorUserSerializer

    def get(self):
        return MentorUser.objects.all().filter(email=self.request.email)

class MentorProfileListUser(generics.ListAPIView):
    '''returns one profile'''
    def get(self):
        return 'gotten'

class MentorProfileUpdate(generics.UpdateAPIView):
    '''update one profile'''
    def update(self):
        return 'update'

class MentorProfileDestroy(generics.DestroyAPIView):
    '''destroy one profile'''
    def destroy(self):
        return 'destroy'

class LoginView(APIView):
    def post(self, request, format=None):
        pass

class LogoutView(APIView):
    def post(self, request, format=None):
        pass
