from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class Supervisor(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=7, unique=True)
    designation = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    year_of_exp = models.IntegerField(default=0)
    specialization = models.CharField(max_length=20, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Notification(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    def __str__(self):
        return self.note
 
class Project(models.Model):
    project_name = models.CharField(max_length=20)
    department = models.CharField(max_length=45, null=True, default=None)
    year = models.CharField(max_length=30, null=True, default=None)
    type_of_project = models.CharField(max_length=25, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    progress = models.DecimalField(max_digits=4, decimal_places=1, default = 0.0)
    group_name = models.CharField(max_length=20, null=True, default=None)
    member1 = models.CharField(max_length=20, null=True, default=None)
    member2 = models.CharField(max_length=20, null=True, default=None)
    member3 = models.CharField(max_length=20, null=True, default=None)
    member4 = models.CharField(max_length=20, null=True, default=None)
    def __str__(self):
        return self.project_name
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateField(null=True, default=None)
    task_heading = models.CharField(max_length=20)
    task_details = models.CharField(max_length=500)
    weightage = models.IntegerField()
    status = models.BooleanField(default = False)
    note = models.CharField(max_length=200,  null=True, default=None)
    def __str__(self):
        return self.task_heading
    
class Super_Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateField(null=True, default=None)
    task_heading = models.CharField(max_length=20)
    task_details = models.CharField(max_length=500)
    weightage = models.IntegerField()
    status = models.BooleanField(default = False)
    def __str__(self):
        return self.task_heading
    
class Pre_Task(models.Model):
    deadline = models.DateField(null=True, default=None)
    task_heading = models.CharField(max_length=20)
    task_details = models.CharField(max_length=500)
    weightage = models.IntegerField()
    status = models.BooleanField(default = False)
    def __str__(self):
        return self.task_heading
