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

from .forms import DemoForm # App se DemoForm import kiya

def home_view(request):
    submitted_name = None
    
    if request.method == 'POST':
        form = DemoForm(request.POST) # User ka submitted data receive kiya
        if form.is_valid():
            # Form ka data retrieve kar rahe hain
            submitted_name = form.cleaned_data['name']
            
            # Note: Agar data Database mein permanent store karna hai, 
            # toh ModelForm use karke form.save() karna padta hai.
    else:
        form = DemoForm() # Empty form GET request par load hoga

    return render(request, 'home.html', {
        'form': form,
        'submitted_name': submitted_name
    })