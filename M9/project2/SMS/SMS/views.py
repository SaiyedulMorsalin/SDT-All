from django.http import HttpResponse

def contact(request):
    return HttpResponse("This is contact Page....")

def homepage(request):
    return HttpResponse("This is Home Page....")
