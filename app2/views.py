from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>THAGGEDELE.......</h1>')

def second(request):
    return HttpResponse('<h2>pushpa ante fire.....</h2>')
