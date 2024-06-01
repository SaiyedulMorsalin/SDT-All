from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Plase Go App Homepage -->>http://127.0.0.1:8000/first_app/")