from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, RetrieveView, DestroyView, UpdateView
from admin import admin

urlpatterns = {
    url(r'^menteerequests_admin/', admin.site.urls),
    url(r'^menteerequests/$', CreateView.as_view(), name="create"),
    url(r'^menteerequests/$', ListView.as_view(), name="list"),
    url(r'^menteerequests/$', RetrieveView.as_view(), name="retrieve"),
    url(r'^menteerequests/$', DestroyView.as_view(), name="destroy"),
    url(r'^menteerequests/$', UpdateView.as_view(), name="update"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
