from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = {
    url(r'^become_mentor$', views.become_mentor, name='become_mentor'),
    url(r'^find_mentor$', views.find_mentor, name='find_mentor'),
    url(r'^need_mentor$', views.need_mentor, name='need_mentor'),
    url(r'^mentor_login$', views.mentor_login, name='Mentor_Login'),
    url(r'^reset_password$', views.reset_password, name='Reset Password'),
    url(r'^mentor_logout$', views.mentor_logout, name='Logout'),
    url(r'^$', views.index, name='index'),
    url(r'^view_portfolio/(?P<id>\d+)/$', views.view_portfolio, name='view_portfolio'),

}
urlpatterns = format_suffix_patterns(urlpatterns)
