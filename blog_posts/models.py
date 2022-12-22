from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default=None)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


