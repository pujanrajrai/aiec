from admindash.models import ApplyAsStudent
from django.shortcuts import render, redirect
from django.contrib import messages


def student_applications(request):
    search = request.GET.get('search', None)
    context = {
        'current': 'student_applications',
        'active': 'student_applications',
    }
    if search == "read":
        context["active_tab"] = "read"
        context["applications"] = ApplyAsStudent.objects.filter(
            is_read=True).order_by('-create_date')
    else:
        context["applications"] = ApplyAsStudent.objects.filter(
            is_read=False).order_by('-create_date')
        context["active_tab"] = "unread"

    return render(request, 'student_applications/list.html', context)


def student_application_mark_as_read(request):
    try:
        application = ApplyAsStudent.objects.get(pk=request.POST.get('pk'))
        application.is_read = True
        application.save()
        messages.success(
            request, f'Student application from {application.full_name} has been marked as read.')
    except:
        messages.error(request, 'Task failed... Something went wrong')
    return redirect(request.META['HTTP_REFERER'])
