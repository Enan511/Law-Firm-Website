from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content_file', 'image', 'date_published', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_published': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        content_file = cleaned_data.get('content_file')

        if not content_file:
            raise forms.ValidationError('Please provide content or upload a file.')
        return cleaned_data
