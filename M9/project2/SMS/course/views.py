from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def course(request):
    return HttpResponse("This is course1 --Django....")

def home(request):
    return HttpResponse("This is course home page...")
