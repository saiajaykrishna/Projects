from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE , null = True, blank = True)
    Title  = models.CharField(max_length = 100)
    descreption = models.TextField(max_length = 500, blank = True, null = True)
    complete = models.BooleanField(default = False)
    created  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ['complete']