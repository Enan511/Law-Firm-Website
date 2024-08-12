from django import forms
from .models import News, Comment
from ckeditor.fields import RichTextField


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image', 'date_published', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': RichTextField(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_published': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')

        if not content:
            raise forms.ValidationError('Please provide content.')
        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
