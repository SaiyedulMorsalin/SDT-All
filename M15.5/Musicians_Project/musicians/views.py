from django.shortcuts import render,redirect
from .forms import MusicianForm

# Create your views here.

def musician_form(request):
    
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            redirect('home_page')
    else:
        form = MusicianForm()
    return render(request,'musician_form.html',{'form':form})
        