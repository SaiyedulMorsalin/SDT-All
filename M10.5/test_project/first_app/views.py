from django.shortcuts import render

# Create your views here.
def home_page(request):
    d ={'author':'hasin hayder','age':45,'address':'Rangpur','lst':[10,20,30,40,50]}
    return render(request,'index.html', context=d)
