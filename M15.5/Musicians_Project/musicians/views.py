from django.shortcuts import render
from .forms import MusicianForm
# Create your views here.

def musician_form(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
        return render(request,'musician_form.html',{'form':form})
    else:
        form = MusicianForm()
        return render(request,'musician_form.html',{'form':form})
        