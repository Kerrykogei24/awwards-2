"""Awwards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

urlpatterns = [
    url('admin/', admin.site.urls),
    url('accounts/', include('django_registration.backends.one_step.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('',include('rate.urls')),
    url('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
