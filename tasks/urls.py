from . import views
from django.urls import path

urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('add/', views.add_task_view, name='add_task'),
    path('complete/<int:task_id>/', views.mark_complete_view, name='mark_complete'),
]