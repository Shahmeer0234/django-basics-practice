from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Menu

def home(request):
    return HttpResponse('Hi Shahmeer How are you?')

def menu_by_id(request, menu_id):
    menu = Menu.objects.get(pk = menu_id)
    return HttpResponse(f"{menu.menu_item}: tpye of {menu.cuisine} cuisine")