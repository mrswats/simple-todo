from django.conf import settings
from django.db import models


class TaskState(models.TextChoices):
    TODO = ("To Do", "To Do")
    DONE = ("DONE", "DONE")


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(
        max_length=50, choices=TaskState.choices, default=TaskState.TODO
    )
    title = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)

    @property
    def is_completed(self) -> bool:
        return self.state == TaskState.DONE

    def complete_task(self) -> None:
        self.state = TaskState.DONE
        self.save()

    def __str__(self) -> str:
        return self.title
