from django.shortcuts import render,redirect
from . forms import PracticeForm,PDForm

# Create your views here.
# def home(request):
#     if request.method =='POST':
#         form = PracticeForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
            
#             return render(request,'home.html',{'form':form})
#     form = PracticeForm()
#     return render(request,'home.html',{'form':form})

def home(request):
    if request.method =='POST':
        form = PDForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            
            return render(request,'home.html',{'form':form})
    form = PDForm()
    return render(request,'home.html',{'form':form})