from django.shortcuts import render, redirect
from .forms import AlbumForm
from django.contrib import messages

def album_forms(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            print(form.cleaned_data)
            messages.success(request, 'Album saved successfully!')
            # return redirect('album_forms')  # Change 'album_forms' to the name of your view or another appropriate URL
    else:
        form = AlbumForm()
    
    return render(request, 'album_forms.html', {'form': form})
