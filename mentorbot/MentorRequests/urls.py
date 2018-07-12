from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, RetrieveView, DestroyView, UpdateView

urlpatterns = {
    url(r'^mentorrequests/$', CreateView.as_view(), name="create"),
    url(r'^mentorrequests/$', ListView.as_view(), name="list"),
    url(r'^mentorrequests/$', RetrieveView.as_view(), name="retrieve"),
    url(r'^mentorrequests/$', DestroyView.as_view(), name="destroy"),
    url(r'^mentorrequests/$', UpdateView.as_view(), name="update"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
