import json
import requests
from rest_framework import status
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt
from decouple import config

api_url = config('API_URL')
headers = {
            'Content-Type': 'application/json'
            }

def index(request):
    return render(request, '../templates/index.html')

def mentor_field(request):
    response = requests.get(api_url + 'mentorshipfield_display/', headers=headers)
    return response

def carousel(request):
    response = requests.get(api_url + 'users/', headers=headers)
    return response

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
        print('-----images', image)

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
            "first_name": firstname,
            "last_name": lastname,
            "email": email,
            "username": username,
            "password": password
            }
        response = requests.post(api_url + 'register', headers=headers, data=User)
        if response.status_code is 200:
            profile = requests.post(api_url + 'add_profile/' , headers=headers, data=UserProfile)
        else:
            return HttpResponse('Fail', headers)
        return HttpResponse(response, profile, headers)

def find_mentor(request):
    if request.method == 'GET':
        return render(request, '../templates/find_mentor.html')
    elif request.method == 'POST':
        field_name = request.POST.get('search')
        data = {"field_name": field_name}
        print('-----data', data)
        response = requests.get(api_url + 'mentorshipfield_search/', headers=headers, data=data)
        print('-----response1', response)
        if not response:
            return render(request, '../templates/find_mentor.html')
        else:
            return render(request, '../templates/find_mentor.html', {'get_all_mentors': response})


# def mentor_profile(request):
#     view_mentor = MentorDetails.objects.get(
#         email='angelamutava@gmail.com')
#     # import pdb;pdb.set_trace()
#     return render(request, '../templates/profile.html', {
        # 'view_mentor': view_mentor})


def view_portfolio(request, id):
    # get_mentor = MentorDetails.objects.get(id=id)
    if request.method == 'GET':
        return render(request, '../templates/porfolio.html')
    elif request.method == 'POST':
        return 'working on it'


def account_activation_sent(request):
    return render(request, '../templates/emails/account/activation.html')


def messenger_find_mentor(request):
    return render(request, '../templates/messenger_find_mentor.html')

def messenger_become_mentor(request):
    return render(request, '../templates/messenger_become_mentor.html')

def error_404(request):
    return render(request, '../templates/error_404.html')
