from django.db import models

# Create your models here.

# model used for the database of user's todos.
class TodoListItem(models.Model):
    content = models.TextField(blank=False)