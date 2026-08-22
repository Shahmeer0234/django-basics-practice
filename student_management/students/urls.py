from django.urls import path
from . import views

urlpatterns = [
    #path('', views.student_list),
    path('api/students/', views.student_list, name='student_list'),
    path('', views.home_view, name='home'),
]