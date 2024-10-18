from django.db import models
from django.conf import settings


class TaskState(models.TextChoices):
    TODO = ("To Do", "To Do")
    DONE = ("DONE", "DONE")


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(max_length=50, choices=TaskState.choices, default=TaskState.TODO)
    title = models.CharField(max_length=255)
    description = models.TextField()
