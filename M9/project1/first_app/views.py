from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_app(request):
    return HttpResponse("This is inside the firstapp..")


def courses(request):
    return HttpResponse("this is firstapp course page....")