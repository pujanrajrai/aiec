from django.shortcuts import render, redirect
from django.contrib import messages
from admindash.models import ApplyAsAgent


def agent_applications(request):
    search = request.GET.get('search', None)
    context = {
        'current': 'agent_applications',
        'active': 'agent_applications',
    }
    if search == "read":
        context["active_tab"] = "read"
        context["applications"] = ApplyAsAgent.objects.filter(
            is_read=True).order_by('-create_date')
    else:
        context["applications"] = ApplyAsAgent.objects.filter(
            is_read=False).order_by('-create_date')
        context["active_tab"] = "unread"

    return render(request, 'agent_applications/list.html', context)


def agent_application_mark_as_read(request):
    try:
        application = ApplyAsAgent.objects.get(pk=request.POST.get('pk'))
        application.is_read = True
        application.save()
        messages.success(
            request, f'Agent application from {application.full_name} has been marked as read.')
    except:
        messages.error(request, 'Task failed... Something went wrong')
    return redirect(request.META['HTTP_REFERER'])
