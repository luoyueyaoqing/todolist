from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    nickname = models.CharField(verbose_name="昵称", max_length=32, null=True, blank=True)

    def __str__(self):
        return self.nickname or self.username


class Todo(models.Model):
    user = models.ForeignKey(to=User, related_name="tasks")
    task = models.CharField(max_length=128)
    complete = models.BooleanField()
    create_time = models.DateTimeField(default=timezone.now)
    complete_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.user, self.complete, self.task[:20])