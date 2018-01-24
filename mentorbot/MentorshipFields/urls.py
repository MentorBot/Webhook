from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, RetrieveView, DestroyView, UpdateView

urlpatterns = {
    url(r'^mentorshipfields/$', CreateView.as_view(), name="create"),
    url(r'^mentorshipfields/$', ListView.as_view(), name="list"),
    url(r'^mentorshipfields/$', RetrieveView.as_view(), name="retrieve"),
    url(r'^mentorshipfields/$', DestroyView.as_view(), name="destroy"),
    url(r'^mentorshipfields/$', UpdateView.as_view(), name="update"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
