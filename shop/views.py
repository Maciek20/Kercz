from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world! You'ra at the shop!")

def login(request):
    return HttpResponse("Logowanie")
