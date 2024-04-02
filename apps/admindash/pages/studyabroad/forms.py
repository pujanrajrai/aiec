from django import forms
from admindash.models import Category, Title
from django_ckeditor_5.widgets import CKEditor5Widget


class StudyAbroadForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title', 'quoatation', 'image',
                  'secondary_image', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Study Abroad Title'}),
            'quoatation': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Small Quote'}),
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
        }
        labels = {
            'quoatation': "Quote",
            'title': "Study Abroad Title",
            "secondary_image": "Blog Image"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['secondary_image'].required = True
        self.fields['quoatation'].required = True
