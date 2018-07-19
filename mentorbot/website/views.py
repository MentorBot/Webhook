from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt
from MentorDetails.models import MentorUser, MentorProfile
from decouple import config

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from MenteeRequests.models import MenteeRequests
# from tokens import account_activation_token
api_url = config('API_URL')
headers = {
            'Content-Type': 'application/json'
            }

def index(request):
    return render(request, '../templates/index.html')

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

        data = {
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
        response = requests.post(api_url + 'register', headers=headers, data=data )
        return response

def find_mentor(request):
    if request.method == 'GET':
        return render(request, '../templates/find_mentor.html')
    elif request.method == 'POST':
        field_name = request.POST.get('search')
        data = {"field_name": field_name}
        response = request.post(api_url + 'mentorshipfield_search/', headers=headers, data=data)
        if response is 200:
            data = request.json()
            return render(request, '../templates/display_mentors.html', {mentor: data})

        else:
            return render(request, '.../templates/')


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


    # if request.method == 'POST':
    #     name = str(request.POST.get('name'))
    #     email = str(request.POST.get('email'))
    #     phone_number = request.POST.get('number')
    #     location = str(request.POST.get('location'))
    #     bio = str(request.POST.get('bio'))
    #     mentee_request = MenteeRequests(
    #         mentee_name=name, phone_number=phone_number, email=email,
    #         location=location, short_bio=bio, mentor=get_mentor)
    #     mentee_request.save()
    #     return render(request, '../templates/porfolio.html',
    #                   {"get_mentor": get_mentor})



# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = MentorDetails.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, MentorDetails.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.active = True
#         user.profile.email_confirmed = True
#         user.save()
#         login(request, user)
#         return redirect('index')
#     else:
#         return render(request, 'activation_invalid.html')



def account_activation_sent(request):
    return render(request, '../templates/emails/account/activation.html')


def messenger_find_mentor(request):
    return render(request, '../templates/messenger_find_mentor.html')

def messenger_become_mentor(request):
    return render(request, '../templates/messenger_become_mentor.html')

def error_404(request):
    return render(request, '../templates/error_404.html')
