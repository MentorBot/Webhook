from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from MentorDetails.models import MentorUser, MentorProfile


def index(request):
    return render(request, '../templates/index.html')


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
        facebook = str(request.POST.get('burl'))
        image = str(request.POST.get('image'))
        short_bio = str(request.POST.get('bio'))
        view = MentorUser.objects.filter(email=request.POST.get('email'))
        if view:
            print('user already exists.')
            return render(request, '../templates/become_mentor.html')

        else:
            mentor = MentorDetails(name=name, phone_number=phone_number,
                                   email=email, twitter=twitter, github=github,
                                   linkdin=linkdin,
                                   mentorship_field=mentorship_field,
                                   medium=medium,
                                   facebook=facebook, image=image,
                                   short_bio=short_bio)
            mentor.save()
            return render(request, '../templates/index.html')

        return render(request, '../templates/become_mentor.html')
    return render(request, '../templates/become_mentor.html')

def find_mentor(request):
    if request.POST.get('search'):
        search = request.POST.get('search')
        get_all_mentors = MentorDetails.objects.all().filter(
            Q(mentorship_field__icontains=search) | Q(
                name__icontains=search))
    else:
        get_all_mentors = MentorDetails.objects.all().filter(
            mentor_status=False)
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
