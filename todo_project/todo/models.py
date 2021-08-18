from django.db import models

# Create your models here.


class SingleTodo(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
