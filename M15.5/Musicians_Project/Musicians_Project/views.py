from django.shortcuts import render
from musicians.models import MusicianModel

def home_page(request):
    data = MusicianModel.objects.all()
    return render(request,'home.html',{'data':data})