from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task, Supervisor, Project
from django.contrib.auth.models import User


# Create your views here.

@login_required
def home(response): 
    project = Project.objects.get(user=response.user)
    tasks = Task.objects.filter(user=response.user)
    return render(response, "main/home.html", {'tasks':tasks,"project":project})

@login_required
def notif(response):
    return render(response, "main/Notif.html", {})

@login_required
def profile(response):
    project = Project.objects.get(user=response.user)
    supervisor = Supervisor.objects.get(name=project.supervisor)
    return render(response, "main/profile.html", {"project":project,"supervisor":supervisor})