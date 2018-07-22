from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = {
    url(r'^become_mentor$', views.become_mentor, name='become_mentor'),
    url(r'^find_mentor$', views.find_mentor, name='find_mentor'),
    url(r'^login$', views.login, name='Login'),
    url(r'^edit$', views.edit, name='Edit'),
    url(r'^logout$', views.logout, name='Logout'),
    url(r'^$', views.index, name='index'),
    url(r'^view_portfolio/(?P<id>\d+)/$', views.view_portfolio, name='view_portfolio'),

}
urlpatterns = format_suffix_patterns(urlpatterns)
