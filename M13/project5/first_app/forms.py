from django import forms
from django.core import validators
#widgets == field to html input
# class contactForm(forms.Form):
#     name = forms.CharField(label='User Name',help_text='must added sure name',required=False,widget=forms.Textarea(attrs={'id':'text-area','class':'class1 class2','placeholder':'Enter your name'}))
#     email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    # appoint = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    # Choose = [('s','Small'),('M','Medium')]
    # size = forms.ChoiceField(choices=Choose,widget=forms.RadioSelect())
    # MEAL = [('P','Peperoni'),('M','Mashroom')]
    # pizza = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)
    # age = forms.CharField(widget=forms.NumberInput())
    # file = forms.FileField()
    
    
class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name',widget=forms.TextInput({'placeholder':"Enter Your Name"}))
    # email = forms.CharField(label='Student Name',widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) <10:
    #         raise form.ValueError("Enter a Name with at least 10 characters")
    #     return valname





class contactForm(forms.Form):
    name = forms.CharField(label='Student Name',widget=forms.TextInput({'placeholder':"Enter Your Name"}),validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 characters')])
    email = forms.EmailField(label='User Email',validators=[validators.EmailValidator])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])