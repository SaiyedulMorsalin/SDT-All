from django.shortcuts import render
from album.models import AlbumModel
def home_page(request):
    data = AlbumModel.objects.all()
    return render(request,'index.html',{'data':data})

