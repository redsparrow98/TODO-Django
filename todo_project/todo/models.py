from django.db import models


class SingleTodo(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
