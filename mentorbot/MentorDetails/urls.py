from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
<<<<<<< HEAD
from .views import MentorDetailsCreateUser, MentorDetailsListUsers, MentorDetailsListUser, MentorDetailsUpdate, MentorDetailsDestroy,  MentorProfileCreate, MentorProfileDestroy, MentorProfileListUser, MentorProfileListUsers, MentorProfileUpdate, LoginView, LogoutView
# from MentorDetails import views
from .admin import admin

urlpatterns = {
    url(r'^register$', MentorDetailsCreateUser.as_view(), name="create"),
    url(r'^users/$', MentorDetailsListUsers.as_view(), name="list"),
    url(r'^user/$', MentorDetailsListUser.as_view(), name="list_user"),
    url(r'^delete/$', MentorDetailsDestroy.as_view(), name="destroy"),
    url(r'^update/$', MentorDetailsUpdate.as_view(), name="update"),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    url(r'^add_profile/$', MentorProfileCreate.as_view(), name="create_profile"),
    url(r'^profiles/$', MentorProfileListUsers.as_view(), name="list_profiles"),
    url(r'^profile/$', MentorProfileListUser.as_view(), name="list_profile"),
    url(r'^update_profile/$', MentorProfileUpdate.as_view(), name="update_profile"),
    url(r'^delete_profile/$', MentorProfileDestroy.as_view(), name="destroy_profile"),

    url(r'^auth/', include('social_django.urls', namespace='social')),
=======
from .views import CreateView, ListView, RetrieveView, DestroyView, UpdateView

urlpatterns = {
    url(r'^mentordetails/$', CreateView.as_view(), name="create"),
    url(r'^mentordetails/$', ListView.as_view(), name="list"),
    url(r'^mentordetails/$', RetrieveView.as_view(),
        name="retrieve"),
    url(r'^mentordetails/$', DestroyView.as_view(),
        name="destroy"),
    url(r'^mentordetails/$', UpdateView.as_view(),
        name="update"),
>>>>>>> implement mentor functionality.
}

urlpatterns = format_suffix_patterns(urlpatterns)
