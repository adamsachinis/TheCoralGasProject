from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. From the app re arxidi! You're at the polls index.")

def index2(request):
    return HttpResponse("Hello, world. From the app re arxidi gamimeno auto einai to index 2! You're at the polls index.")


