from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=80)
    complete = models.BooleanField(default=False)
    # time = models.DateTimeField(default=12)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.title