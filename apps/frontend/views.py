from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from admindash.models import Category, Title
from .forms import ContactForm, ApplyAsStudentForm, ApplyAsAgentForm
# Create your views here.
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    context = {
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations")
    }
    return render(request, 'frontend/home.html', context)


def title(request, pk):
    context = {
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "title": Title.objects.get(pk=pk)
    }
    return render(request, 'frontend/title.html', context)


def aboutus(request):
    context = {
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations")
    }
    return render(request, 'frontend/aboutus.html', context)


def contactus(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            messages.success(
                request, 'Thank you for your message we will get back to you soon.')
            # Redirect back to the current page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        "form": form,
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations")
    }
    return render(request, 'frontend/contactus.html', context)


def applyasstudent(request):
    form = ApplyAsAgentForm()
    if request.method == 'POST':
        form = ApplyAsAgentForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            messages.success(
                request, 'Thank you for applying.We will get back soon')
            # Redirect back to the current page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        "form": form,
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations")
    }
    return render(request, 'frontend/applyasstudent.html', context)


def applyasagent(request):
    form = ApplyAsAgentForm()
    if request.method == 'POST':
        form = ApplyAsAgentForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            messages.success(
                request, 'Thank you for applying.We will get back to you soon')
            # Redirect back to the current page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {
        "form": form,
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations")
    }
    return render(request, 'frontend/applyasagent.html', context)


def allblogs(request):
    blog_list = Title.objects.filter(category__name="blogs")
    paginator = Paginator(blog_list, 9)  # Show 10 blogs per page

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    # Calculate the range of page numbers to display
    current_page = blogs.number
    total_pages = paginator.num_pages
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)

    page_range = range(start_page, end_page + 1)

    context = {
        'blogs': blogs,
        'page_range': page_range,
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations")
    }
    return render(request, 'frontend/blogs.html', context)
