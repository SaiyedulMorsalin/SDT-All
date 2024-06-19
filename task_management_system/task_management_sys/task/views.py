from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = TaskForm()
    return render(request,'task.html',{'form':form})

def edit_task(request,id):
    
    current_task = TaskModel.objects.get(pk =id)
    form = TaskForm(instance=current_task)
    if request.method =='POST':
        form = TaskForm(request.POST,instance=current_task)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    return render(request,'task.html',{'form':form})
        
    

def delete_task(request,id):
    current_task= TaskModel.objects.get(pk = id)
    current_task.delete()
    return redirect('home_page')

