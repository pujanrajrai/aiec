from django import forms
from admindash.models import SubCategory
from django_ckeditor_5.widgets import CKEditor5Widget


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', 'placeholder': 'Enter Download File Title'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['image'].required = True
