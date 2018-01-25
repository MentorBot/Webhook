from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, RetrieveView
from admin import admin

urlpatterns = {
    url(r'^bot_admin/', admin.site.urls),
    url(r'^bot/$', CreateView.as_view(), name="create"),
    url(r'^bot/$', ListView.as_view(), name="list"),
    url(r'^bot/$', RetrieveView.as_view(), name="retrieve"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
