
from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    title = forms.CharField(label="Enter Todo" , max_length=80, 
    widget=forms.TextInput(attrs={'placeholder':'Enter Todo'}))
    desc = forms.CharField(label="Description \n", 
    widget=forms.Textarea(attrs={'placeholder':'Enter description', 'name':'body', 'rows':'4', 'cols':'50'}))
    # time = forms.TimeField()

    class Meta:
        model = Todo
        fields = ['title', 'desc']

    