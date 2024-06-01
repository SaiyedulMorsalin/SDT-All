from django.shortcuts import render
import datetime
# Create your views here.
def home_page(request):
    d ={'author':'hasin hayder','age':45,'address':'Rangpur','lst':[10,20,30,40,50],'description':'Django Template Engine provides filters which are used to transform the values of variables and tag arguments.','birthday':datetime.datetime.now(),'empty':"",'courses':[
        {'name':"introduction to c programming!",'duration':'3 months','fees':"5000"},
        {'name':"introduction to C++ programming!",'duration':'4 months','fees':"6500"},
        {'name':"introduction to DSA ",'duration':'6 months','fees':"7000"}
    ],'birth':datetime.date(2024,6,1),'comment_date': datetime.date(2024, 6, 1)}
    return render(request,'index.html', context=d)
