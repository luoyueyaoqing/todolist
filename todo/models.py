from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    GENDER_OPTIONS = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )
    nickname = models.CharField(verbose_name='昵称', max_length=60, null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_OPTIONS, default=0)
    info = models.TextField(verbose_name='个人说明', blank=True, null=True)

    def user_gender(self, gender):
        if gender == '男':
            self.gender = 1
        elif gender == '女':
            self.gender = 2
        else:
            self.gender = 0
        return self.gender

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
