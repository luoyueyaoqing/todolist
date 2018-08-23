from django.db import models
from django.utils import timezone

class Task(models.Model):
    task = models.CharField(max_length=128)
    complete = models.BooleanField()
    create_time = models.DateTimeField(default=timezone.now)
    complete_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.complete, self.task[:20])