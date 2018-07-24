from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import main



urlpatterns = {
    # url(r'^become_mentor$', views.become_mentor, name='become_mentor'),
    # url(r'^find_mentor$', views.find_mentor, name='find_mentor'),
    # url(r'^need_mentor$', views.need_mentor, name='need_mentor'),
    # url(r'^mentor_login$', views.mentor_login, name='Mentor_Login'),
    # url(r'^reset_password$', views.reset_password, name='Reset Password'),
    # url(r'^mentor_logout$', views.mentor_logout, name='Logout'),
    # url(r'^$', views.index, name='index'),
    # url(r'^view_portfolio/(?P<id>\d+)/$', views.view_portfolio, name='view_portfolio'),


    url(r'^$', main.index, name='index'),
    url(r'^become_mentor$', main.become_mentor, name='become_mentor'),
    url(r'^find_mentor$', main.find_mentor, name='find_mentor'),
    url(r'^view_portfolio/(?P<id>\d+)/$', main.view_portfolio,
        name='view_portfolio'),
    url(r'^view_profile/(?P<id>\d+)/$', main.mentor_profile,
        name='view_profile'),
    url(r'^account_activation_sent/$', main.account_activation_sent,
        name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        main.activate, name='activate'),
    url(r'^account_login/$', main.account_login,
        name='account_login'),
    url(r'^account_email/$', main.account_email,
        name='account_email'),
    url(r'^account_signup/$', main.account_signup,
        name='account_signup'),
    url(r'^account_setup/(?P<id>\d+)$', main.account_setup,
        name='account_setup'),
    url(r'^logout/$', main.logout_view,
        name='logout'),

}
urlpatterns = format_suffix_patterns(urlpatterns)
