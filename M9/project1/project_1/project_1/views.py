from django.http import HttpResponse

def homepage(request):
    return HttpResponse("You're currenty see homepage")

def contact(request):
    return HttpResponse("This is Contact Page!!!")