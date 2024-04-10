from django import forms
from admindash.models import Category, Title
from django_ckeditor_5.widgets import CKEditor5Widget


class DownloadsForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['sub_category', 'title',  'files']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Download File Title'}),
            'sub_category': forms.Select(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Download File Title'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['files'].required = True
        self.fields['sub_category'].required = True
