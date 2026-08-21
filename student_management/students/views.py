from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student

def student_list(request):
    students = Student.objects.all()

    return HttpResponse(f"<h1>Total Students: {Student.count()}</h1>")

from django.http import JsonResponse
from .models import Student

def student_list(request):
    students = list(Student.objects.values('name', 'roll_number'))
    return JsonResponse(students, safe=False)