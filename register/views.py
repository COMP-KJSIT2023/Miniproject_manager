from django.shortcuts import render, redirect
from .forms import Registerform, LoginForm, Superform
from main.models import Supervisor, Task, Super_Task, Project, Pre_Task
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
import string, random

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string

def has_permission(user):
    user = User.objects.get(username=user)
    return  user.groups.filter(name='Supervisor').exists()

def task_exist(super_task):
    return Task.objects.filter(task_heading=super_task.task_heading).exists()

def migrate_super_tasks(user,code):
    supervisor = Supervisor.objects.get(code=code).user
    super_tasks = Super_Task.objects.filter(user = supervisor)
    for super_task in super_tasks:
        if not task_exist(super_task):
            Task.objects.create(
                user=user,
                deadline=super_task.deadline,
                task_heading=super_task.task_heading,
                task_details=super_task.task_details,
                weightage=super_task.weightage,
                status=False
            )

def migrate_pre(user):
    pre_tasks = Pre_Task.objects.all()
    for pre_task in pre_tasks:
            Super_Task.objects.create(
                user=user,
                deadline=None,
                task_heading=pre_task.task_heading,
                task_details=pre_task.task_details,
                weightage=pre_task.weightage,
                status=False
            )

def register(response):
    if response.method == "POST":
        form = Registerform(response.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Normal User')
            user.groups.add(group)
            code=response.POST.get("Supervisor")
            supervisor = Supervisor.objects.get(code=code)
            user = User.objects.get(username=response.POST.get("username"))
            gname = form.cleaned_data["Group_name"]
            m1 = form.cleaned_data["Group_member_1"]
            m2 = form.cleaned_data["Group_member_2"]
            m3 = form.cleaned_data["Group_member_3"]
            m4 = form.cleaned_data["Group_member_4"]
            name = response.POST.get("Project")
            year = response.POST.get("year")
            department = response.POST.get("department") 
            type_of_project = response.POST.get("type_of_project")
            supervisor.project_set.create(
                project_name = name, 
                user=user, 
                progress=0.0, 
                group_name=gname, 
                member1=m1,
                member2=m2,
                member3=m3, 
                member4=m4,
                department = department,
                year = year,
                type_of_project = type_of_project)  
        return redirect("/login")
    else:
        form = Registerform()
    return render(response, "registration/register.html", {"form":form})

def supervisor(response):
    if response.method == "POST":
        form = Superform(response.POST) 
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data["first_name"] + " "+ form.cleaned_data["last_name"]
            year_of_exp = form.cleaned_data["year_of_exp"]
            specialization = form.cleaned_data["specialization"]
            designation = response.POST.get("designation")
            department = response.POST.get("department") 
            Supervisor.objects.create(
                user=user, name=name, 
                code=generate_random_string(6).upper(), 
                designation=designation, 
                department=department, 
                year_of_exp=year_of_exp, 
                specialization=specialization)
            
            group = Group.objects.get(name='Supervisor')
            user.groups.add(group)
            try:
                migrate_pre(user)
            except:
                print("Couldnt migrate")
            
            return redirect("/login")
    else:
        form = Superform()
    return render(response, "registration/supervisor.html", {"form": form})


def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                auth_login(response, user)
                if has_permission(user):
                    return redirect('/super/')
                else:
                    supervisor = Project.objects.get(user=user).supervisor
                    migrate_super_tasks(user, supervisor.code)
                    return redirect('/')
            else:
                return render(response, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(response, "registration/login.html", {"form":form})