from django import forms
from admindash.models import ContactUs, ApplyAsStudent, ApplyAsAgent


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'phone_number', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', "id": "name", 'placeholder': 'Enter Your Full Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2 mb-2', "id": "email", 'placeholder': 'Enter Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', "id": "subject", 'placeholder': 'Enter Subject*'}),
            'message': forms.Textarea(attrs={'class': 'form-control mt-2 mb-2', "id": "message", "rows": "5", 'placeholder': 'Enter Message*'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control mt-2 mb-2', "id": "name", 'placeholder': 'Enter Phone Number*'}),
        }


class ApplyAsAgentForm(forms.ModelForm):
    class Meta:
        model = ApplyAsAgent
        fields = ['full_name', 'education', 'consultancy_name', 'address',
                  'phone_number', 'email', 'years_of_experience', 'remarks']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName5'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEducation'}),
            'consultancy_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputConsultancyName'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputAddress'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputPhoneNumber'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail'}),
            'years_of_experience': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputExperience'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px', 'id': 'inputRemarks'}),
        }


class ApplyAsStudentForm(forms.ModelForm):
    FACULTY_CHOICES = [
        ('', 'Choose...'),  # Empty option as placeholder
        ('Science', 'Science'),
        ('Management', 'Management'),
        ('Humanities', 'Humanities'),
    ]

    COUNTRY_CHOICES = [
        ('', 'Choose...'),  # Empty option as placeholder
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('United Kingdom', 'United Kingdom'),
        ('USA', 'USA'),
        ('Europe', 'Europe'),
        ('New Zeeland', 'New Zeeland'),
    ]

    ENGLISH_TEST_CHOICES = [
        ('', 'Choose...'),  # Empty option as placeholder
        ('IELTS', 'IELTS'),
        ('PTE', 'PTE'),
        ('TOEFL', 'TOEFL'),
        ('Japanease Language', 'Japanease Language'),
    ]

    full_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputName5'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputPhoneNumber'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'inputEmail'}))
    # date_of_birth = forms.DateField(widget=forms.DateInput(
    #     attrs={'class': 'form-control', 'id': 'inputDateOfBirth'}))
    faculty = forms.ChoiceField(choices=FACULTY_CHOICES, widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'inputFaculty'}))
    pass_out_year = forms.CharField(max_length=4, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputPassOutYear'}))
    percentage = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'id': 'inputPercentage'}))
    apply_for_country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'inputApplyForCountry'}))
    english_proficiency_test = forms.ChoiceField(choices=ENGLISH_TEST_CHOICES, widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'inputEnglishProficiencyTest'}))
    score = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'inputScore'}))
    remarks = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'inputRemarks'}))

    class Meta:
        model = ApplyAsStudent
        fields = ['full_name', 'phone_number', 'email', 'date_of_birth', 'faculty', 'pass_out_year',
                  'percentage', 'apply_for_country', 'english_proficiency_test', 'score', 'remarks']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName5'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputPhoneNumber'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': "date", 'id': 'inputDateOfBirth'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputFaculty'}),
            'pass_out_year': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputPassOutYear'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control', 'id': 'inputPercentage'}),
            'apply_for_country': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputApplyForCountry'}),
            'english_proficiency_test': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEnglishProficiencyTest'}),
            'score': forms.TextInput(attrs={'class': 'form-control', 'id': 'inputScore'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'id': 'inputRemarks'}),
        }
