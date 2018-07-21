import os
import json
import requests
from rest_framework import status
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt
from decouple import config
from mentorbot.settings.base import MEDIA_ROOT

api_url = config('API_URL')
headers = {
            'Content-type': 'application/json'
            }

def index(request):
    return render(request, '../templates/index.html')

def mentor_field(request):
    response = requests.get(api_url + 'mentorshipfield_display/', headers=headers)
    return response

def carousel(request):
    response = requests.get(api_url + 'users/', headers=headers)
    return response

def save_image(email, image):
    filename = email
    data =  image
    path = default_storage.save('../templates/images/profile_pictures', ContentFile(data.read()))
    tmp_file = os.path.join(MEDIA_ROOT, path)
    return tmp_file

@csrf_exempt
def become_mentor(request):
    if request.method == 'GET':
        return render(request, '../templates/become_mentor.html')
    elif request.method == 'POST':
        firstname = str(request.POST.get('firstname'))
        lastname = str(request.POST.get('lastname'))
        email = str(request.POST.get('email'))
        phone_number = int(request.POST.get('phone'))
        twitter = str(request.POST.get('twitter'))
        github = str(request.POST.get('gitlink'))
        linkdin = str(request.POST.get('linkedin'))
        mentorship_field = str(request.POST.get('sfield'))
        medium = str(request.POST.get('burl'))
        image = request.FILES.get('image')
        facebook = str(request.POST.get('fblink'))
        short_bio = str(request.POST.get('bio'))
        password = str(request.POST.get('password'))
        username = firstname + '_' + lastname
        print('---old image', image)

        image = save_image(email, image)
        print('-----new image', image)

        UserProfile = {
            "first_name": firstname,
            "last_name": lastname,
            "email": email,
            "username": username,
            "phone_number": phone_number,
            "twitter": twitter,
            "github": github,
            "linkdin": linkdin,
            "mentorship_field": mentorship_field,
            "medium": medium,
            "image": image,
            "facebook": facebook,
            "short_bio": short_bio,
            "password": password
            }
        User = {
            "email": email,
            "username": username,
            "password1": password,
            "password2": password

            }
        data = json.dumps(User)
        data1 = json.dumps(UserProfile)
        response = requests.post(api_url + 'rest-auth/registration/', data=data, headers=headers)
        print('------response', response.text)
        if response.status_code is 201:
            profile = requests.post(api_url + 'add_profile/', data=data1, headers=headers)
            if profile.status_code is 201:
                return HttpResponse('User added succesfully', headers)
            else:
                return HttpResponse('fail to add profile', headers)
        else:
            return HttpResponse('Fail', headers)
        return HttpResponse(response, profile, headers)

def find_mentor(request):
    if request.method == 'GET':
        return render(request, '../templates/find_mentor.html')
    elif request.method == 'POST':
        field_name = request.POST.get('search')
        data = {"field_name": field_name}
        data = json.dumps(data)
        print('-----data', data)
        response = requests.get(api_url + 'mentorshipfield_search/', params=data, headers=headers)
        count = response.content.count
        # count = count._content.count
        print('-----response1', response)
        print('-------count', count)
        if count == 0:
            return render(request, '../templates/find_mentor.html', {'error': 'error'})
        else:
            return render(request, '../templates/find_mentor.html', {'get_all_mentors': response})

def view_portfolio(request, id):
    # get_mentor = MentorDetails.objects.get(id=id)
    if request.method == 'GET':
        return render(request, '../templates/porfolio.html')
    elif request.method == 'POST':
        return 'working on it'


def account_activation_sent(request):
    return render(request, '../templates/emails/account/activation.html')

def need_mentor(request):
    email = request.POST.get('email')
    data = {"email": email}
    data = json.dumps(data)
    message = requests.post(api_url + 'need_mentor/', data=data, headers=headers)
    if message.status_code is 201:
        return render(request, '../templates/find_mentor.html', {'message': 'message'})


def login(self, request, format=None):
    email = str(request.POST.get('email'))
    password = str(request.POST.get('password'))
    user = {
        "email": email,
        "password": password
    }
    data = json.dumps(user)
    response = requests.get(api_url + 'rest-auth/login/', data=data, headers=headers)
    return response

def logout(self, request, format=None):
    response = requests.get(api_url + 'rest-auth/logout/', headers=headers)
    return response

def error_404(request):
    return render(request, '../templates/error_404.html')
