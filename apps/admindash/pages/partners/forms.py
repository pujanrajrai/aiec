from django import forms
from admindash.models import Category, Title
from django_ckeditor_5.widgets import CKEditor5Widget


class PartnersForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title', 'image', 'link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Partners Title'}),
            'link': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter the link'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
