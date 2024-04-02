from django import forms
from admindash.models import Category, Title
from django_ckeditor_5.widgets import CKEditor5Widget


class StoriesForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title', 'quoatation', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Student Name'}),
            'quoatation': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter University and Degree name'}),

            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }
        labels = {
            'title': 'Student Name',
            'quoatation': 'University and Degree Name',
            'description': 'Success Stories',
        }
