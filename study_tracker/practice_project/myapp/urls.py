from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('profile/', views.profile),
    path('services/', views.services),
]