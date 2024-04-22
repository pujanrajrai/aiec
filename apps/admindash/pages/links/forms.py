from django import forms
from admindash.models import Category, Title
from django_ckeditor_5.widgets import CKEditor5Widget


class LinksForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Usefull link title'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter link'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['link'].required = True
