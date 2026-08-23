from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=10)
    is_enrolled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.PROTECT, related_name='students')

    def __str__(self):
        return self.name