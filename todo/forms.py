from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'description']
        model = Todo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
