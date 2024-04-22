# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from admindash.models import Title, Category
from .forms import LinksForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class LinksCreateView(CreateView):
    model = Title
    form_class = LinksForm
    template_name = 'links/create.html'
    success_url = reverse_lazy('admindash:pages:links:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'links'
        return context

    def form_valid(self, form):
        default_category = Category.objects.get(name='links')
        form.instance.category = default_category
        messages.success(self.request, 'links created successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class LinksListView(ListView):
    model = Title
    template_name = 'links/list.html'
    context_object_name = 'links'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__name="links")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'links'
        return context


@method_decorator(login_required, name='dispatch')
class LinksUpdateView(UpdateView):
    model = Title
    form_class = LinksForm
    template_name = 'links/update.html'
    success_url = reverse_lazy('admindash:pages:links:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'links'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'links updated successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class LinksDeleteView(DeleteView):
    success_url = reverse_lazy('admindash:pages:links:list')

    def get(self, request, *args, **kwargs):
        # Retrieve the object to delete
        obj = get_object_or_404(Title, pk=kwargs['pk'])
        # Delete the object
        obj.delete()
        messages.success(self.request, 'Links deleted successfully.')
        # Redirect to the success URL
        return redirect(self.success_url)
