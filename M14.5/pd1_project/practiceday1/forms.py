from django import forms 
import datetime
from . models import PracticeModel
class PracticeForm(forms.Form):
    # Common Fields
    name = forms.CharField(initial='Your Name')
    comment = forms.CharField(widget=forms.Textarea)
    comment1 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(required=False,label='Enter Your Email')
    date = forms.DateField()
    birth_date = forms.CharField(widget=forms.NumberInput(attrs={'type':'date'}))
    YEAR_CHOICE = ['2000','2001','2002','2003']
    birth_day = forms.DateField(widget=forms.SelectDateWidget(years = YEAR_CHOICE))
    value = forms.DecimalField(initial=10)
    message = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Enter your message within 20 characters'}))
    date_today = forms.DateField(initial=datetime.date.today)
    agree = forms.BooleanField()
    # ChoiceField, MultipleChoiceField, ModelChoiceField, and ModelMultipleChoiceField
    FAVORITE_COLORS = [('white','White'),('black','Black'),('rose','Rose Black')]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS)
    select_color = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS)
    multi_color = forms.MultipleChoiceField(choices=FAVORITE_COLORS)


class PDForm(forms.ModelForm):
    class Meta:
       model = PracticeModel
       fields = '__all__'