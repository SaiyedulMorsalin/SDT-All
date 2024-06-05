from django.shortcuts import render
from .forms import contactForm,StudentForm
# Create your views here.
def home_page(request):
    return render(request,'first_app/index.html')

def about(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
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
    if request.method =='POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' +file.name,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'./first_app/django_form.html',{'form':form})
    else:
        form = contactForm()
    return render(request,'./first_app/django_form.html',{'form':form})
        

def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'./first_app/django_form.html',{'stu_form':form})
    else:
        form = StudentForm()
        return render(request,'./first_app/django_form.html')