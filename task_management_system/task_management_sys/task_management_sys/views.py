from django.shortcuts import render
from task.models import TaskModel

def home_page(request):
    data = TaskModel.objects.all()
    return render(request,'index.html',{'data':data})