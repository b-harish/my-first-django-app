from django.db import models
from django.utils import timezone

# Create your models here.
class ToDoItem(models.Model):
    '''Model representing a to-do item.'''
    text = models.TextField(help_text='Enter a task to add to the list ...')
    created_date = models.DateTimeField(default=timezone.now)
    done_date = models.DateTimeField(blank=True, null=True)

    def complete(self):
        self.done_date = timezone.now()

    def __str__(self) -> str:
        return self.text