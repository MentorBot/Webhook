import os
import re
import json
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate, logout
from django.utils.encoding import force_text
from django.urls import reverse
from decouple import config
from django.views.decorators.csrf import csrf_exempt


api_url = config('API_URL')
headers = {
            'Content-type': 'application/json'
            }


from MentorDetails.models import MentorUser, MentorProfile
from MenteeRequests.models import MenteeRequests
# from bot.models import Profile
from website.tokens import account_activation_token


def index(request):
    return render(request, '../templates/index.html')

def check_email_exists(email):
    if MentorUser.objects.filter(email=email).exists():
        return True
    return False

def become_mentor(request):
    if request.method == 'POST':
        first_name = str(request.POST.get('firstname'))
        last_name = str(request.POST.get('lastname'))
        email = str(request.POST.get('email'))
        phone_number = int(request.POST.get('phone'))
        twitter = str(request.POST.get('twitter'))
        github = str(request.POST.get('gitlink'))
        linkdin = str(request.POST.get('linkedin'))
        mentorship_field = str(request.POST.get('sfield'))
        medium = str(request.POST.get('burl'))
        avatar = request.FILES.get('image')
        facebook = str(request.POST.get('fblink'))
        short_bio = str(request.POST.get('bio'))

        if check_email_exists(email):
            messages.warning(
                request, 'Oops user with the email already exists.')
            return render(request, '../templates/become_mentor.html')

        else:
            mentor = MentorUser(email=email)
            mentor.save()
            profile = MentorProfile(user=mentor, phone_number=phone_number,
                              twitter=twitter, github=github, linkdin=linkdin,
                              mentorship_field=mentorship_field, medium=medium,
                              first_name=first_name, last_name=last_name,
                              avatar=avatar,facebook=facebook, short_bio=short_bio)
            profile.save()
            messages.success(
                request, 'Registration successful. \
                Account activation email sent.')

            subject = 'Activate Your Mentorbot Account'
            domain = config('DOMAIN')
            uid = urlsafe_base64_encode(force_bytes(mentor.pk)).decode()
            token = account_activation_token.make_token(mentor)
            activation_link = reverse('activate', args=[uid, token])
            activation_url = "{}{}".format(domain, activation_link)
            message = render_to_string('account_activation_email.html', {
                'mentor': mentor,
                'activation_url': activation_url
            })
            mentor.email_user(subject, message)
            return redirect('account_activation_sent')
    return render(request, '../templates/become_mentor.html')

def find_mentor(request):
    if request.POST.get('search'):
        search = request.POST.get('search')
        get_mentors = MentorProfile.objects.filter(
            Q(mentorship_field__icontains=search) | Q(
                first_name__icontains=search) | Q(
                last_name__icontains=search))
        return render(request, '../templates/find_mentor.html',
                  {'get_mentors': get_mentors})
    else:
        get_all_mentors = MentorUser.objects.all().filter(
            is_active=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(get_all_mentors, 8)
    try:
        get_all_mentors = paginator.page(page)
    except PageNotAnInteger:
        get_all_mentors = paginator.page(1)
    except EmptyPage:
        get_all_mentors = paginator.page(paginator.num_pages)

    return render(request, '../templates/find_mentor.html',
                  {'get_all_mentors': get_all_mentors})

def mentor_profile(request, id):
    try:
        view_mentor = MentorUser.objects.get(
            id=id)
        return render(request, '../templates/profile.html', {
            'view_mentor': view_mentor})
    except MentorUser.DoesNotExist:
        return render(request, '../templates/account_login.html')
@csrf_exempt
def view_portfolio(request, id):
    try:
        get_mentor = MentorUser.objects.get(id=id)
        if request.method == 'POST':
            name = str(request.POST.get('name'))
            email = str(request.POST.get('email'))
            phone_number = request.POST.get('number')
            location = str(request.POST.get('location'))
            bio = str(request.POST.get('bio'))
            mentee_request = MenteeRequests(
                mentee_name=name, phone_number=phone_number, email=email,
                location=location, bio=bio, mentor=get_mentor)
            mentee_request.save()
            messages.success(
                request, 'Request sent successfully.\
                    Wait for mentor approval. Thanks.')
            return render(request, '../templates/porfolio.html',
                        {"get_mentor": get_mentor})
        else:
            return render(request, '../templates/porfolio.html',
                        {"get_mentor": get_mentor})
    except MentorUser.DoesNotExist:
        return render(request, '../templates/index.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        mentor = MentorUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, MentorUser.DoesNotExist):
        mentor = None

    if mentor is not None and account_activation_token.check_token(
            mentor, token):
        mentor.is_active = True
        x = mentor.profile.mentor_status
        mentor.profile.mentor_status = True
        y = mentor.profile.mentor_status
        mentor.profile.save()
        mentor.save()
        return redirect('account_setup', id=mentor.id)

    else:
        return render(request, '../templates/account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, '../templates/account_activation_sent.html')


def account_setup(request, id):
    try:
        mentor = MentorUser.objects.get(
            id=id)

        if request.method == 'POST':
            password = str(request.POST.get('password'))
            confpassword = str(request.POST.get('confpassword'))
            if password == confpassword:
                mentor.password = password
                mentor.save()
                return redirect('account_login')
            else:
                messages.warning(
                    request, 'Passwords do not match.'
                )
                return render(request, '../templates/account_setup.html',
                {'mentor':mentor})
        else:
            messages.warning(
                    request, 'Passwords do not match.'
                )
            return render(request, '../templates/account_setup.html',
                {'mentor':mentor})

    except MentorUser.DoesNotExist:
        messages.warning(
                request, 'Mentor does not exist.')
        return render(request, '../templates/account_activation_sent.html')




def account_login(request):
    if request.method == 'POST':
        username = str(request.POST.get('email'))
        password = str(request.POST.get('password'))
        if username and password:
            try:
                mentor = MentorUser.objects.get(email=username,
                                                    password=password)
                if mentor is not None:
                    if mentor.is_active:
                        # login(request, mentor)
                        messages.success(
                            request, 'Login Successful.'
                        )
                        return redirect('view_profile', id=mentor.id)
                    else:
                        # Return a 'disabled account' error message
                        messages.warning(
                            request, 'Account has been deactivated.')
                        return render(request, '../templates/aacount_login.html')
                else:
                    # Return an 'invalid login' error message.
                    messages.warning(
                        request, 'Invalid login credentials')
                    return render(request, '../templates/account_login.html')
            except MentorUser.DoesNotExist:
                messages.warning(
                        request, 'Invalid login credentials')
                return render(request, '../templates/account_login.html')

        else:
            messages.warning(
                request, 'Fill in username and password.')
    else:
        return render(request, '../templates/account_login.html')


def account_email(request):
    return render(request, '../templates/account_login.html')


def account_signup(request):
    return render(request, '../templates/account_login.html')


def logout_view(request):
    logout(request)
    return render(request, '../templates/account_login.html')
