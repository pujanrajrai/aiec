from captcha.fields import CaptchaField
from django import forms


class CaptchaFieldForm(forms.Form):
    captcha = CaptchaField()
