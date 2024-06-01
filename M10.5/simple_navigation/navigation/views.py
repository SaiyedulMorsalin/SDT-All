from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'navigation/home.html')

def about_page(request):
    return render(request,'navigation/about.html')

def blog_page(request):
    return render(request,'navigation/blog.html')
