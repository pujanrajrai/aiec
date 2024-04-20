from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from admindash.models import Category, Title, SubCategory
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
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "active": "home"
    }
    return render(request, 'frontend/home.html', context)


def title(request, slug):
    title = Title.objects.get(slug=slug)
    active = "null"
    if title.category.name == "testpreparations":
        active = "testpreparations"
    elif title.category.name == "studyabroad":
        active = "studyabroad"

    elif title.category.name == "services":
        active = "services"

    context = {
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "title": title,
        "active": active
    }
    return render(request, 'frontend/title.html', context)


def aboutus(request):
    context = {
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "active": "aboutus"

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
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "active": "contactus"
    }
    return render(request, 'frontend/contactus.html', context)


def applyasstudent(request):
    form = ApplyAsStudentForm()
    if request.method == 'POST':
        form = ApplyAsStudentForm(request.POST)
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
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "active": "apply"
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
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "active": "apply"

    }
    return render(request, 'frontend/applyasagent.html', context)


def allblogs(request):
    blog_list = Title.objects.filter(
        category__name="blogs").order_by('-pk')
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
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "active": "blog"

    }
    return render(request, 'frontend/blogs.html', context)


def downloads(request):
    category = SubCategory.objects.all()
    context = {
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
        "category": category
    }
    return render(request, 'frontend/downloads.html', context)


def downloads_details(request, sub_category):
    context = {
        "downloads": Title.objects.filter(
            category__name="downloads").filter(sub_category__name=sub_category).order_by('pk'),
        "sub_category": sub_category,
        "studies": Title.objects.filter(category__name="studyabroad"),
        "services": Title.objects.filter(category__name="services"),
        "partners": Title.objects.filter(category__name="partners"),
        "stories": Title.objects.filter(category__name="stories"),
        "testpreparations": Title.objects.filter(category__name="testpreparations"),
    }
    return render(request, 'frontend/downloads_details.html', context)

# def downloads(request):
#     download_list = Title.objects.filter(
#         category__name="downloads").order_by('sub_category')
#     paginator = Paginator(download_list, 30)  # Show 10 blogs per page

#     page = request.GET.get('page')
#     try:
#         downloads = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         downloads = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         downloads = paginator.page(paginator.num_pages)

#     # Calculate the range of page numbers to display
#     current_page = downloads.number
#     total_pages = paginator.num_pages
#     start_page = max(1, current_page - 2)
#     end_page = min(total_pages, current_page + 2)

#     page_range = range(start_page, end_page + 1)

#     context = {
#         'downloads': downloads,
#         'page_range': page_range,
#         "studies": Title.objects.filter(category__name="studyabroad"),
#         "services": Title.objects.filter(category__name="services"),
#         "partners": Title.objects.filter(category__name="partners"),
#         "stories": Title.objects.filter(category__name="stories"),
#         "testpreparations": Title.objects.filter(category__name="testpreparations"),
#         "active": "downloads"

#     }
#     return render(request, 'frontend/downloads.html', context)


def admin(request):
    return redirect("admindash:login")
