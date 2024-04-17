from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Project, Supervisor, Task, Super_Task
from django.contrib.auth.models import User

def migrate_super_tasks(supervisor, super_task):
    projects = Project.objects.filter(supervisor=supervisor)
    users = [project.user for project in projects]
    for user in users:
        Task.objects.create(
            user=user,
            deadline=super_task.deadline,
            task_heading=super_task.task_heading,
            task_details=super_task.task_details,
            weightage=super_task.weightage,
            status=False
        )
            
@login_required
def home(response):
    current_supervisor = Supervisor.objects.get(user=response.user)
    projects = Project.objects.filter(supervisor=current_supervisor)
    project_data = []
    for project in projects:
        tasks = Task.objects.filter(user = project.user)
        completed=0.0
        total=0.0
        for task in tasks:
            if task.status:
                completed += task.weightage
            total += task.weightage
        if total is 0.0:
            total = 1.0    
        project.progress = completed/total*100
        project.save()
        username = User.objects.get(id=project.user_id).username
        project_data.append({'project': project, 'username': username})
    return render(response, "supervisor/home.html", {'projects': project_data})

@login_required 
def index(response,pk):
    current_user = Project.objects.get(id=pk).user
    tasks = Task.objects.filter(user=current_user)
    
    if response.method == "POST":
        if response.POST.get("create"):
            return redirect('create', pk=pk)
        if response.POST.get("save"):
            for task in tasks:
                if response.POST.get("task_"+ str(task.id)) == "on":
                    task.status = True
                else:
                    task.status = False
                task.note = response.POST.get("note_"+str(task.id))
                task.save()
            return redirect('index', pk)
        for task in tasks:
            if response.POST.get("delete_"+ str(task.id)):
                task.delete()
                return redirect('index', pk)
    return render(response, "supervisor/index.html", {"tasks":tasks})


@login_required
def create(response,pk):
    if response.POST.get("newItem"):
        n1 = response.POST.get("newtaskhead")
        n2 = response.POST.get("newtaskbody")
        d = response.POST.get("deadline")
        weight = response.POST.get("Weight")
        user = Project.objects.get(id=pk).user
        Task.objects.create(user=user, deadline = d, task_heading = n1, task_details = n2, weightage = weight, status = False)
        return redirect('/super/')
    return render(response, "supervisor/create.html", {"user":User})


def add_task(response):
    if response.POST.get("newItem"):
        n1 = response.POST.get("newtaskhead")
        n2 = response.POST.get("newtaskbody")
        d = response.POST.get("deadline")
        weight = response.POST.get("Weight")
        user = response.user
        supervisor = Supervisor.objects.get(user=user)
        Super_Task.objects.create(user=user, deadline = d, task_heading = n1, task_details = n2, weightage = weight, status = False)
        super_task = Super_Task.objects.get(user=user, deadline = d, task_heading = n1, task_details = n2, weightage = weight, status = False)
        migrate_super_tasks(supervisor, super_task)
        return redirect('/super/')
    return render(response, "supervisor/add_task.html", {})

def profile(response):
    supervisor = Supervisor.objects.get(user=response.user)
    return render(response, "supervisor/profile.html", {"supervisor":supervisor})