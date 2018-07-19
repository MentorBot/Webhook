from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, RetrieveView, DestroyView, UpdateView
from .admin import admin

urlpatterns = {
    url(r'^mentorshipfield_add/$', CreateView.as_view(), name="create"),
    url(r'^mentorshipfield_display/$', ListView.as_view(), name="list"),
    url(r'^mentorshipfield_search/$', RetrieveView.as_view(), name="retrieve"),
    url(r'^mentorshipfield_delete/$', DestroyView.as_view(), name="destroy"),
    url(r'^mentorshipfield_edit/$', UpdateView.as_view(), name="update"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
