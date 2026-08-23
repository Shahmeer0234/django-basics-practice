from django.db import models

# Create your models here.

CATEGORY = [
    ('study', 'Study'),
    ('uni', 'Uni'),
    ('coding', 'Coding'),
    ('personal', 'Personal')
]

class Task(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY, max_length=20, default='Coding')
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title