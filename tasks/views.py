from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Task
from .forms import ModelForm

def task_list_view(request):
    pending_tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)
    
    return render(request, 'tasks_list.html', {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    })

def add_task_view(request):

    if request.method == 'POST':
        form = ModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = ModelForm()

    return render(request, 'add_task.html', {'form':form})

def mark_complete_view(request, task_id):
    
    task = get_object_or_404(Task, id=task_id)
    
    task.is_completed = True
    
    task.save()
    
    return redirect('task_list')