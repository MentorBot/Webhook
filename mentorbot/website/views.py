import os
import re
import json
import requests
from rest_framework import status
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.files.storage import FileSystemStorage
from decouple import config
from mentorbot.settings.base import MEDIA_ROOT, EMAIL_HOST_USER
from .email import *
from MentorDetails.models import MentorUser

api_url = config('API_URL')
headers = {
            'Content-type': 'application/json'
            }

def index(request):
    return render(request, '../templates/index.html')

def mentor_field():
    response = requests.get(api_url + 'mentorshipfield_display/', headers=headers)
    return response

def send_email(subject, reciever,sender, message):
    send_mail(
    subject,
    message,
    sender,
    reciever,
    fail_silently=False,
)

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def check_email_exists(email):
    if MentorUser.objects.filter(email=email).exists():
        return True
    return False

@csrf_exempt
def become_mentor(request):
    if request.method == 'GET':
        mentor_fields = mentor_field()
        return render(request, '../templates/become_mentor.html', {"mentor_field": mentor_fields})
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
        facebook = str(request.POST.get('fblink'))
        short_bio = str(request.POST.get('bio'))
        password = str(request.POST.get('password'))

        if not email and password:
            return render(request, '../templates/become_mentor.html', {'notification': 'Email and password is needed to create and account!'})

        if not email:
            return render(request, '../templates/become_mentor.html', {'notification': 'Email needed to create and account!'})

        if not firstname and lastname:
            return render(request, '../templates/become_mentor.html', {'notification': 'Please enter first and last name'})

        if not password:
            return render(request, '../templates/become_mentor.html', {'notification': 'Password is needed to create and account!'})

        if not validateEmail( email ):
            return render(request, '../templates/become_mentor.html', {'notification': 'This is not a valid email'} )

        if check_email_exists(email):
            return render(request, '../templates/become_mentor.html', {'notification': 'This email is already in use!'} )



        UserProfile = {
            "first_name": firstname,
            "last_name": lastname,
            "phone_number": phone_number,
            "twitter": twitter,
            "github": github,
            "linkdin": linkdin,
            "mentorship_field": mentorship_field,
            "medium": medium,
            "facebook": facebook,
            "short_bio": short_bio,
            "password": password
            }
        User = {
            "email": email,
            "password": password
            }

        data = json.dumps(User)
        data1 = json.dumps(UserProfile)
        response = requests.post(api_url + 'auth/register', data=data, headers=headers)
        print('----r.sc', response.status_code)
        print('-----r.c',  response.content)
        if response.status_code is 201:
            profile = requests.post(api_url + 'add_profile/', data=data1, headers=headers)
            print('----r.sc', profile.status_code)
            print('-----r.c',  profile.content)
            if profile.status_code is 201:
                send_email('Mentor Activation', email, EMAIL_HOST_USER, activation)
                return render(request, '../templates/become_mentor.html', {'success_message': 'success_message'} )
            else:
                requests.delete(api_url + 'delete_user_no_profile/', data=data, headers=headers)
                return render(request, '../templates/become_mentor.html', {'error': 'error'} )
        else:
                response = response.content
                response = response.decode()
                y = json.loads(response)
                return render(request, '../templates/become_mentor.html', {'user_error': y} )

def find_mentor(request):
    if request.method == 'GET':
        return render(request, '../templates/find_mentor.html')
    elif request.method == 'POST':
        field_name = request.POST.get('search')
        data = {"field_name": field_name}
        data = json.dumps(data)
        response = requests.get(api_url + 'mentorshipfield_search/', params=data, headers=headers)
        count = response.content
        count = count.decode()
        y = json.loads(count)
        x = y.get('count')
        if x == 0:
            return render(request, '../templates/find_mentor.html', {'error': 'error'})
        else:
            return render(request, '../templates/find_mentor.html', {'get_all_mentors': response})

def view_portfolio(request, id):
    get_mentor = requests.get(api_url + 'profile/', data=id, headers=headers)

    if request.method == 'GET':
        return render(request, '../templates/porfolio.html', {"get_mentor": get_mentor})

    elif request.method == 'POST':
        name = str(request.POST.get('name'))
        email = str(request.POST.get('email'))
        phone_number = request.POST.get('number')
        location = str(request.POST.get('location'))
        bio = str(request.POST.get('bio'))
        data = {
            "mentor_details": get_mentor,
            "mentee_name": name,
            "email": email,
            "phone_number": phone_number,
            "location": location,
            "bio": bio
        }
        data = json.dumps(data)
        response = requests.post(api_url + 'request_mentorship/', data=data, headers=headers)
        if response.status_code is 201:
            return render(request, '../templates/porfolio.html', {'message': 'message'})



def account_activation_sent(request):
    return render(request, '../templates/emails/account/activation.html')

@csrf_exempt
def need_mentor(request):
    print('-----r', request)
    email = request.POST.get('email')
    field = request.POST.get('field')
    data = {"requester_email": email, "requested_field": field}
    print('-------- need mentor', data)
    data = json.dumps(data)
    message = requests.post(api_url + 'store_need_mentor_requests', data=data, headers=headers)
    if message.status_code is 201:
        return render(request, '../templates/find_mentor.html', {'message': 'message'})

@csrf_exempt
def mentor_login(request):
    if request.method == 'GET':
        return render(request, '../templates/login.html')
    elif request.method == 'POST':
        email = str(request.POST.get('email'))
        password = str(request.POST.get('password'))
        user = {
            "email": email,
            "password": password
        }
        data = json.dumps(user)
        response = requests.post(api_url + 'auth/login', data=data, headers=headers)
        if response.status_code is 200:
            print('-----chilli', response)
            get_mentor = response.data
            return render(request, '../templates/profile.html', {"get_mentor": get_mentor})
        else:
            if response.status_code is not 200:
                r = response.content
                print('----login', r)
                error = "not happening"
                return render(request, '../templates/login.html'), {'error': error}

def reset_password(request):
    if request.method == 'GET':
        return render(request, '../templates/login.html')
    elif request.method == 'POST':
        return render(request, '../templates/login.html')

def mentor_logout(request):
    response = requests.get(api_url + 'auth/logout', headers=headers)
    return response

def error_404(request):
    return render(request, '../templates/error_404.html')
