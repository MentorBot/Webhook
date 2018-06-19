from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, DestroyView, UpdateView
from MentorDetails import views
from .admin import admin

urlpatterns = {
    url(r'^mentordetails/$', CreateView.as_view(), name="create"),
    url(r'^mentordetails/$', ListView.as_view(), name="list"),
    url(r'^mentordetails/$', RetrieveView.as_view(), name="retrieve"),
    url(r'^mentordetails/$', DestroyView.as_view(), name="destroy"),
    url(r'^mentordetails/$', UpdateView.as_view(), name="update"),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
}

urlpatterns = format_suffix_patterns(urlpatterns)
