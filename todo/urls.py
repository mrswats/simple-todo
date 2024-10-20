from django.contrib import admin
from django.urls import path

from todo.views import add_task
from todo.views import add_task_submit
from todo.views import delete_task
from todo.views import landing
from todo.views import login
from todo.views import task_completed
from todo.views import tasks

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing, name="landing"),
    path("login/", login, name="login"),
    path("tasks/", tasks, name="tasks"),
    path("tasks/add/", add_task, name="add-task"),
    path("tasks/add/submit/", add_task_submit, name="submit-task"),
    path("tasks/delete/<str:task_id>/", delete_task, name="delete-task"),
    path("tasks/complete/<str:task_id>/", task_completed, name="task-completed"),
]
