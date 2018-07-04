from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = {
    url(r'^become_mentor$', views.become_mentor, name='become_mentor'),
    url(r'^find_mentor$', views.find_mentor, name='find_mentor'),
    url(r'^$', views.index, name='index'),
}
urlpatterns = format_suffix_patterns(urlpatterns)
