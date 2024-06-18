from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import AlbumModel
# Create your views here.
def album_form_page(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    form = AlbumForm()
    return render(request,'album_forms.html',{'form':form})

def edit_album(request,id):
    edit_album = AlbumModel.objects.get(pk = id)
    form = AlbumForm(instance=edit_album)
    if request.method == 'POST':
        form = AlbumForm(request.POST,instance=edit_album)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request,'album_forms.html',{'form':form})

def delete_album(request,id):
    delete_album = AlbumModel.objects.get(pk = id)
    delete_album.delete()
    return redirect('home_page')