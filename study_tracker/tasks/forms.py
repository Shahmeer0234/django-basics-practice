from django import forms
from tasks.models import Task

class ModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'due_date']

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }

form = ModelForm()