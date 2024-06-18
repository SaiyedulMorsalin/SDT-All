from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import MusicianModel
# Create your views here.
def musician_home_page(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_form_page')
    form = MusicianForm()    
    return render(request,'musician_index.html',{'form':form})

def edit_musician(request,id):
    musician = MusicianModel.objects.get(pk = id)
    form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('album_form_page')
    return render(request,'musician_index.html',{'form':form})