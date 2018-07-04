from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import requests
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt

from MentorDetails.models import MentorUser, MentorProfile


def index(request):
    return render(request, '../templates/index.html')

def become_mentor(request):
    return render(request, '../templates/become_mentor.html')

    # data = {
    #     "first_name": firstname,
    #     "last_name":lastname,
    #     "email": email,
    #     "phone_number": phone,
    #     "twitter": twitter,
    #     "githublink": gitlink,
    #     "mentorship_field": sfield,
    #     "medium": burl,
    #     "facebook": fblink,
    #     "linkdin": linkedin,
    #     "short_bio": bio,
    #     "image": image
    # }
    # response = requests.post('http://mentorbot-prod.herokuapp.com/register')
    # mentor_response = response.json()



    #         return render(request, '../templates/index.html')

    #     return render(request, '../templates/become_mentor.html')
    # return render(request, '../templates/become_mentor.html')


def find_mentor(request):
    return render(request, '../templates/find_mentor.html')

    # if request.POST.get('search'):
    #     search = request.POST.get('search')
    #     get_all_mentors = MentorDetails.objects.all().filter(
    #         Q(mentorship_field__icontains=search) | Q(
    #             name__icontains=search))
    # else:
    #     get_all_mentors = MentorDetails.objects.all().filter(
    #         mentor_status=False)
    # page = request.GET.get('page', 1)
    # paginator = Paginator(get_all_mentors, 8)
    # try:
    #     get_all_mentors = paginator.page(page)
    # except PageNotAnInteger:
    #     get_all_mentors = paginator.page(1)
    # except EmptyPage:
    #     get_all_mentors = paginator.page(paginator.num_pages)

    # return render(request, '../templates/find_mentor.html',
    #               {'get_all_mentors': get_all_mentors})

def messenger_find_mentor(request):
    return render(request, '../templates/messenger_find_mentor.html')

def messenger_become_mentor(request):
    return render(request, '../templates/messenger_become_mentor.html')

def error_404(request):
    return render(request, '../templates/error_404.html')
