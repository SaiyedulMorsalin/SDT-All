from django import forms
from .models import MusicianModel
class MusicianForm(forms.ModelForm):
    
    class Meta:
        model = MusicianModel
        fields = '__all__'
        widgets = {
            'user_id':forms.NumberInput(attrs={'placeholder':"Please Provide your user id."})
        }