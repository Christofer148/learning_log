"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import re_path

from . import views

urlpatterns = [
    # Login page
    re_path(r'^login/$', LoginView, {'template_name': 'users/login.html'},
            name='login')
]
