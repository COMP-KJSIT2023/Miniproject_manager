from django.contrib import admin
from .models import Supervisor, Task, Project, Notification, Super_Task, Pre_Task

# Register your models here.
admin.site.register(Supervisor)
admin.site.register(Notification)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Super_Task)
admin.site.register(Pre_Task)