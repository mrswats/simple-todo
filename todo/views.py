from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from todo.forms import AddTaskForm
from todo.models import Task


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "todo/login.html", {})


def landing(request: HttpRequest) -> HttpResponse:
    return render(request, "todo/landing.html", {})


def tasks(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.filter(owner=request.user)
    return render(request, "todo/task_list.html", {"tasks": tasks})


def delete_task(request: HttpRequest, task_id: str) -> HttpResponse:
    task = get_object_or_404(Task, pk=task_id, owner=request.owner)
    task.delete()

    return HttpResponseRedirect(reverse("tasks"))


def add_task_submit(request: HttpRequest) -> HttpResponseRedirect:
    form = AddTaskForm(request.POST)
    if form.is_valid():
        form.instance.owner = request.user
        form.save()
        return HttpResponseRedirect(reverse("tasks"))


def add_task(request: HttpRequest) -> HttpResponse:
    form = AddTaskForm()
    return render(request, "todo/task_add.html", {"form": form})


def task_completed(request: HttpRequest, task_id: str) -> None:
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.complete_task()
    return HttpResponseRedirect(reverse("tasks"))
