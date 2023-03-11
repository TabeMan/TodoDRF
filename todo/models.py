from django.db import models

from profiles.models import Profile


class Todo(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
