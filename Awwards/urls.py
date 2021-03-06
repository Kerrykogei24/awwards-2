"""Awwards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from rest_framework.authtoken.views import obtain_auth_token
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('rate.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api-token-auth/', obtain_auth_token),

]