"""Defines URL patterns for learning_logs."""

from django.urls import path, re_path

from . import views

urlpatterns = [
    # Home page
    re_path(r'^$', views.index, name='index'),
]