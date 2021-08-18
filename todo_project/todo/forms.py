from django import forms

from .models import SingleTodo


class SingleTodoForm(forms.ModelForm):

    class Meta:
        model = SingleTodo
        fields = ['title']
