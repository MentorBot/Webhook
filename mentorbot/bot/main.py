from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from MentorDetails.models import MentorDetails
from MenteeRequests.models import MenteeRequests
from tokens import account_activation_token


def index(request):
    return render(request, '../templates/index.html')


def become_mentor(request):
    if request.method == 'POST':

        name = str(request.POST.get('firstname') +
                   ' ' + request.POST.get('lastname'))
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
        view = MentorDetails.objects.filter(email=request.POST.get('email'))
        if view:
            messages.warning(
                request, 'Oops user with the email already exists.',
                extra_tags='alert')
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
            messages.success(
                request, 'Registration successful.', extra_tags='alert')
            # current_site = get_current_site(request)
            # subject = 'Activate Your Mentorbot Account'
            # message = render_to_string(
            #     'emails/account/activation.html', {
            #     'user': mentor,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(mentor.pk)),
            #     'token': account_activation_token.make_token(mentor),
            # })
            # mentor.email_user(subject, message)
            # return redirect('account_activation_sent')
            # return render(request, '../templates/index.html')

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


def mentor_profile(request):
    view_mentor = MentorDetails.objects.get(
        email='angelamutava@gmail.com')
    # import pdb;pdb.set_trace()
    return render(request, '../templates/profile.html', {
        'view_mentor': view_mentor})


def view_portfolio(request, id):
    get_mentor = MentorDetails.objects.get(id=id)
    if request.method == 'POST':
        name = str(request.POST.get('name'))
        email = str(request.POST.get('email'))
        phone_number = request.POST.get('number')
        location = str(request.POST.get('location'))
        bio = str(request.POST.get('bio'))
        mentee_request = MenteeRequests(
            mentee_name=name, phone_number=phone_number, email=email,
            location=location, short_bio=bio, mentor=get_mentor)
        mentee_request.save()
        return render(request, '../templates/porfolio.html',
                      {"get_mentor": get_mentor})
    else:
        return render(request, '../templates/porfolio.html',
                      {"get_mentor": get_mentor})


def account_activation_sent(request):
    return render(request, '../templates/emails/account/activation.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = MentorDetails.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, MentorDetails.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'activation_invalid.html')
