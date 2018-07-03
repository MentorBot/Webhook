from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MentorDetailsCreateUsers, MentorDetailsListUsers, MentorDetailsRetrieveView, MentorDetailsDestroyView,  MentorDetailsUpdateView, LoginView, LogoutView
from MentorDetails import views
from .admin import admin

urlpatterns = {
    url(r'^register$', MentorDetailsCreateUsers.as_view(), name="create"),
    url(r'^profile/$', MentorDetailsListUsers.as_view(), name="list"),
    url(r'^update/$', MentorDetailsRetrieveView.as_view(), name="retrieve"),
    url(r'^delete/$', MentorDetailsDestroyView.as_view(), name="destroy"),
    url(r'^mentordetails/$', MentorDetailsUpdateView.as_view(), name="update"),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
}

urlpatterns = format_suffix_patterns(urlpatterns)
