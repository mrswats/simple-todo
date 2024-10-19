from django.contrib import admin
from django.urls import path

from todo.views import add_task
from todo.views import landing
from todo.views import task_completed
from todo.views import tasks

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing, name="landing"),
    path("tasks/", tasks, name="tasks"),
    path("tasks/add/", add_task, name="add-task"),
    path("tasks/complete/<str:slug>/", task_completed, name="task-completed"),
]
