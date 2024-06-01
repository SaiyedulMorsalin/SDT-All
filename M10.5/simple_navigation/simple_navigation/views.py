
from django.http import HttpResponse

def home(request):
    return HttpResponse("This Home!! please copy this url and enter--->http://127.0.0.1:8000/nav/home/")