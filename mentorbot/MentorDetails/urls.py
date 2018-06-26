from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MentorDetailsCreateView, MentorDetailsListView, MentorDetailsRetrieveView, MentorDetailsDestroyView,  MentorDetailsUpdateView
from MentorDetails import views
from .admin import admin

urlpatterns = {
    url(r'^mentordetails/$', MentorDetailsCreateView.as_view(), name="create"),
    url(r'^mentordetails/$', MentorDetailsListView.as_view(), name="list"),
    url(r'^mentordetails/$', MentorDetailsRetrieveView.as_view(), name="retrieve"),
    url(r'^mentordetails/$', MentorDetailsDestroyView.as_view(), name="destroy"),
    url(r'^mentordetails/$', MentorDetailsUpdateView.as_view(), name="update"),
    # url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
}

urlpatterns = format_suffix_patterns(urlpatterns)
