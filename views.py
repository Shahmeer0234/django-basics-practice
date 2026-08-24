from django.shortcuts import render, get_object_or_404, redirect

# Problem 1
def user_profile_view(request, username):

    role = request.GET.get('role', 'guest')

    return render(request, 'profile.html', {'username':username, 'role': role})

# Problem 2
from .models import Task
def task_detail_view(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    return render(request, 'task_detail.html', {'task', task})

# Problem 3
def create_task_view(request):
    if request.method == 'POST':

        title_input = request.POST.get('title')

        Task.objects.create(title=title_input)

        return redirect('task_list')
    
    else:
        return render(request, 'create_task.html')

# Problem 4
def mark_completed_view(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    task.is_completed = True

    task.save()

    return redirect('task_list')

# Problem 5
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def delete_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.delete()

    return redirect('task_list')

# Problem 6
def search_tasks_view(request):
    query = request.GET.get('q')
    if query:
        task = Task.objects.filter(title__icontains=query)
    else:
        task = Task.objects.all()

    return render(request, 'task_search.html', {'task': task})

# Problem 7
from django.shortcuts import render
from .models import Task

def filter_by_category_view(request):
    query = request.GET.get('category')

    if query:
        task = Task.objects.filter(category=query)
    else:
        task = Task.objects.all()

    return render(request, 'category_list.html', {'task': task})

# Problem 8
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404

def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        
        new_title = request.POST.get('title')
        task.title = new_title
        task.save()

    return render(request, 'edit_task.html', {'task': task})

# Problem 9
from django.shortcuts import redirect, get_object_or_404
from .models import Task

def toggle_task_status_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.is_completed == True:
        task.is_completed = False
    else:
        task.is_completed =True

    task.save()

    return redirect('task_list')

# Problem 10
from django.shortcuts import redirect, get_object_or_404, render
from .models import Task

def master_task_manager_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority')

        if not title:
            return render(request, 'manager.html', {'error': 'Title space cannot be empty!'})

        Task.objects.create(title=title, priority=priority)

        return redirect('task_list')
    else:
        search_query = request.GET.get('search')
        status_query = request.GET.get('status')

        tasks = Task.objects.all()

        if search_query:
            tasks =tasks.filter(title__icontains=search_query)
        
        if status_query == 'completed':
            tasks = tasks.filter(is_completed=True)

        return render(request, 'manager.html', {'tasks':tasks})