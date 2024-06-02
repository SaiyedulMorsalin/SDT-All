from django.shortcuts import render

# Create your views here.
def home(request):
    d = request.GET
    return render(request,'home.html',d)

def about(request):
    d = request.GET
    return render(request,'about.html',d)