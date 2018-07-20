"""mentorbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import refresh_jwt_token
from .settings import base
from django.conf.urls.static import static

urlpatterns = [
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^system_admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^docs/', include_docs_urls(title='mentorbot', public=False)),
    url(r'^', include('bot.urls')),
    url(r'^', include('MenteeRequests.urls')),
    url(r'^', include('MentorDetails.urls')),
    url(r'^', include('MentorRequests.urls')),
    url(r'^', include('MentorshipFields.urls')),
    url(r'^', include('website.urls')),
] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
