from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

from .views import CreateView, ListView, RetrieveView, SearchListView
from . import main


urlpatterns = {
    url('^$', TemplateView.as_view(template_name='index.html')),
    url(r'^bot_add$', CreateView.as_view(), name="create"),
    url(r'^bot_search$', SearchListView.as_view(), name="search"),
    url(r'^bot_list$', ListView.as_view(), name="list"),
    url(r'^bot_list0$', RetrieveView.as_view(), name="retrieve"),
    url(r'^index$', main.index, name='index'),
    url(r'^become_mentor$', main.become_mentor, name='become_mentor'),
    url(r'^find_mentor$', main.find_mentor, name='find_mentor'),
    url(r'^view_portfolio/(?P<id>\d+)/$', main.view_portfolio, name='view_portfolio'),

}
urlpatterns = format_suffix_patterns(urlpatterns)
