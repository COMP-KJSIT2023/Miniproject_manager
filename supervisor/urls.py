from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("<int:pk>/", views.index, name="index"),
path("add_task/", views.add_task, name="add_task"),
path("profile/", views.profile, name="profile"),
path("create/<int:pk>/", views.create, name="create"),
]
