from django.shortcuts import render, redirect
from django.contrib import auth

from .forms import CaptchaFieldForm
# Create your views here.


def login(request):
    context = {"captcha_form": CaptchaFieldForm()}
    if request.user.is_authenticated:
        if request.user:
            return redirect('admindash:pages:blogs:list')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        form = CaptchaFieldForm(request.POST)
        if not form.is_valid():
            context['captcha_errors'] = "Captcha Not Correct"
            context['username'] = username
            return render(request, 'login.html', context)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('admindash:pages:blogs:list')
        else:
            context['errors'] = "User name or password is incorrect"
            context['username'] = username
            return render(request, 'accounts/login.html', context)
    return render(request, 'login.html', context)
