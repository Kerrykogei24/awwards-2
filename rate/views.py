from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
# from rest_framework import viewsets
# from rest_framework import permissions
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# from .token_generator import account_activation_token


def home(request):
    projects = Project.get_projects()
    context={
        'projects' : projects,
    }
    return render(request,"home.html", context)