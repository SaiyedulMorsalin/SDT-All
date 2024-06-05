from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def home_page(request):
    return render(request,'first_app/index.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        select = request.POST.get('select')
        print(request.POST)
        return render(request, 'first_app/about.html', {'name' : name, 'email': email,'select':select})
    else:
        return render(request, 'first_app/about.html')
    
    
def form_page(request):
        return render(request,'first_app/form.html')
    
    
def django_form(request):
    form = contactForm()
    return render(request,'first_app/django_form.html',{'form':form})