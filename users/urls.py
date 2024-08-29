"""Defines URL patterns for users"""

from django.contrib.auth.views import LoginView
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    # Login page
    path('', include("django.contrib.auth.urls")),
    # Logut page
    re_path(r'^logout/$', views.logout_view, name='logout'),
]