from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from todo.models import Task


def landing(request: HttpRequest) -> HttpResponse:
    return render(request, "todo/landing.html", {})


def tasks(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    return render(request, "todo/task_list.html", {"tasks": tasks})


def add_task(request: HttpRequest) -> HttpResponse:
    return render(request, "todo/task_add.html", {})


def task_completed(request: HttpRequest, task_id: str) -> None:
    task = get_object_or_404(Task, id=task_id)
    task.complete_Task()
