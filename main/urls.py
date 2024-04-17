from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("notif/", views.notif, name="notif"),
path("profile/", views.profile, name="profile"),
]
