from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        labels = {
            'task_title': 'Task Title',
            'task_description': 'Task Description',
            'is_completed': 'Completed',
            'task_assign_date': 'Task Assign Date',
            'categories': 'Select Category',
        }
        widgets = {
            'task_assign_date': forms.DateInput(attrs={'type': 'date'}),
        }
