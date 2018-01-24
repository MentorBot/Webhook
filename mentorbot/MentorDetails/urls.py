from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, RetrieveView, DestroyView, UpdateView

urlpatterns = {
    url(r'^mentordetails/$', CreateView.as_view(), name="create"),
    url(r'^mentordetails/$', ListView.as_view(), name="list"),
    url(r'^mentordetails/$', RetrieveView.as_view(), name="retrieve"),
    url(r'^mentordetails/$', DestroyView.as_view(), name="destroy"),
    url(r'^mentordetails/$', UpdateView.as_view(), name="update"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
