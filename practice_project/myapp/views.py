from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>🏠 Home Page</h1>
    <hr>
    <p>My Django Journey...!!</p>

    <a href="/about/">About</a> |
    <a href="/contact/">Contact</a> |
    <a href="/services/">Services</a> |
    <a href="/profile/">Profile</a>
    """)

def about(request):
    return HttpResponse("""<h1>About Me</h1>
    <p>My name is Ali Shahmeer!</p>
    <p>My Age is 20</p>
    <p>I am from Pakistan</p>
    <p>I am Studing in Air University Multan Campus</p>
    """)

def contact(request):
    return HttpResponse("""<h1>My Contact</h1>
    <p>ali.shahmeer@gmail.com</p>
    """)

def services(request):
    return HttpResponse("""
    <h1>Services</h1>
    <p>Python</p>
    <p>Django</p>
    """)

def profile(request):
    return HttpResponse("""
    <h1>Ali Shahmeer</h1>
    <p>Backend Developer</p>
    """)