from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from MentorDetails.models import MentorDetails
from MenteeRequests.models import MenteeRequests
from bot.models import Profile


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
        image = request.FILES.get('image')
        facebook = str(request.POST.get('fblink'))
        short_bio = str(request.POST.get('bio'))
        view = MentorDetails.objects.filter(email=request.POST.get('email'))
        if view:
            messages.warning(
                request, 'Oops user with the email already exists.')
            return render(request, '../templates/become_mentor.html')

        else:
            mentor = MentorDetails(first_name=first_name, last_name=last_name,
                                   email=email, avatar=image)
            mentor.save()
            profile = Profile(user=mentor, phone_number=phone_number,
                              twitter=twitter, github=github, linkdin=linkdin,
                              mentorship_field=mentorship_field, medium=medium,
                              facebook=facebook, short_bio=short_bio)
            profile.save()
            messages.success(
                request, 'Registration successful. \
                Account activation email sent.')
            # current_site = get_current_site(request)
            # subject = 'Activate Your Mentorbot Account'
            # domain = current_site.domain
            # uid = urlsafe_base64_encode(force_bytes(mentor.pk)).decode()
            # token = account_activation_token.make_token(mentor)
            # activation_link = reverse('activate', args=[uid, token])
            # activation_url = "http://{}{}".format(domain, activation_link)
            # message = render_to_string('account_activation_email.html', {
            #     'mentor': mentor,
            #     'activation_url': activation_url
            # })
            # # mentor.email_user(subject, message)
            # return redirect('account_activation_sent')
    return render(request, '../templates/become_mentor.html')


def find_mentor(request):
    if request.POST.get('search'):
        search = request.POST.get('search')
        get_all_mentors = MentorDetails.objects.filter(
            Q(profile__mentorship_field__icontains=search) | Q(
                first_name__icontains=search) | Q(
                last_name__icontains=search))
    else:
        get_all_mentors = MentorDetails.objects.all().filter(
            is_active=False)
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
    view_mentor = MentorDetails.objects.get(
        id=id)
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
        messages.success(
            request, 'Request sent successfully.\
                 Wait for mentor approval. Thanks.')
        return render(request, '../templates/porfolio.html',
                      {"get_mentor": get_mentor})
    else:
        return render(request, '../templates/porfolio.html',
                      {"get_mentor": get_mentor})


# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         mentor = MentorDetails.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, MentorDetails.DoesNotExist):
#         mentor = None

#     if mentor is not None and account_activation_token.check_token(
#             mentor, token):
#         mentor.is_active = True
#         mentor.profile.email_confirmed = True
#         mentor.save()
#         return redirect('account_login')

#     else:
#         return render(request, '../templates/account_activation_invalid.html')


# def account_activation_sent(request):
#     return render(request, '../templates/account_activation_sent.html')


# def account_login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return redirect('view_profile', id=mentor.id)
#         else:
#             # Return a 'disabled account' error message
#     else:
#         # Return an 'invalid login' error message.
#     return render(request, '../templates/account_login.html')
