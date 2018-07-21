from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MentorDetailsCreateUser, MentorDetailsListUsers, MentorDetailsListUser, MentorDetailsUpdateUser , MentorDetailsDestroyUser ,  MentorProfileCreate, MentorProfileDestroy, MentorProfileListUser, MentorProfileListUsers, MentorProfileUpdate, LoginView, LogoutView
from .admin import admin

urlpatterns = {
    url(r'^users/$', MentorDetailsListUsers.as_view(), name="list"),
    url(r'^user/$', MentorDetailsListUser.as_view(), name="list_user"),
    url(r'^delete/$', MentorDetailsDestroyUser.as_view(), name="destroy"),
    url(r'^update/$', MentorDetailsUpdateUser.as_view(), name="update"),

    url(r'^add_profile/$', MentorProfileCreate.as_view(), name="create_profile"),
    url(r'^profiles/$', MentorProfileListUsers.as_view(), name="list_profiles"),
    url(r'^profile/$', MentorProfileListUser.as_view(), name="list_profile"),
    url(r'^update_profile/$', MentorProfileUpdate.as_view(), name="update_profile"),
    url(r'^delete_profile/$', MentorProfileDestroy.as_view(), name="destroy_profile"),

    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^auth/register$', MentorDetailsCreateUser.as_view(), name="auth-register"),
    url(r'^auth/login$', LoginView.as_view(), name="Login"),
    url(r'^auth/logout$', LogoutView.as_view(), name="Logout"),


}

urlpatterns = format_suffix_patterns(urlpatterns)
