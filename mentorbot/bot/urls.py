from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ListView, RetrieveView, SearchListView
from .admin import admin

urlpatterns = {
    url(r'^bot_add$', CreateView.as_view(), name="create"),
    url(r'^bot_search$', SearchListView.as_view(), name="search"),
    url(r'^bot_list$', ListView.as_view(), name="list"),
    url(r'^bot_list0$', RetrieveView.as_view(), name="retrieve"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
