from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>hai good morning</h1>')

def second(request):
    return HttpResponse('<h2>How are you doing</h2>')
    