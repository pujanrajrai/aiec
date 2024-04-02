from admindash.models import ContactUs
from django.shortcuts import render, redirect
from django.contrib import messages


def contact_us(request):
    search = request.GET.get('search', None)
    context = {
        'current': 'contactus',
        'active': 'contactus',
    }
    if search == "read":
        context["active_tab"] = "read"
        context["conatcts"] = ContactUs.objects.filter(
            is_read=True).order_by('-created_date')
    else:
        context["conatcts"] = ContactUs.objects.filter(
            is_read=False).order_by('-created_date')
        context["active_tab"] = "unread"

    return render(request, 'contactus/list.html', context)


def contactus_mark_as_read(request):
    try:
        contactus = ContactUs.objects.get(pk=request.POST.get('pk'))
        contactus.is_read = True
        contactus.save()
        messages.success(
            request, f'Contactus form {contactus.name} has been Marked As Read.')

    except:
        messages.error(request, 'Task Failed... Something Went Wrong')

    return redirect(request.META['HTTP_REFERER'])
