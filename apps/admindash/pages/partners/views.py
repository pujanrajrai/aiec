# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from admindash.models import Title, Category
from .forms import PartnersForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class PartnersCreateView(CreateView):
    model = Title
    form_class = PartnersForm
    template_name = 'partners/create.html'
    success_url = reverse_lazy('admindash:pages:partners:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'partners'
        return context

    def form_valid(self, form):
        default_category = Category.objects.get(name='partners')
        form.instance.category = default_category
        messages.success(self.request, 'partners created successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PartnersListView(ListView):
    model = Title
    template_name = 'partners/list.html'
    context_object_name = 'partners'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__name="partners")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'partners'
        return context


@method_decorator(login_required, name='dispatch')
class PartnersUpdateView(UpdateView):
    model = Title
    form_class = PartnersForm
    template_name = 'partners/update.html'
    success_url = reverse_lazy('admindash:pages:partners:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'partners'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'partners updated successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PartnersDeleteView(DeleteView):
    success_url = reverse_lazy('admindash:pages:partners:list')

    def get(self, request, *args, **kwargs):
        # Retrieve the object to delete
        obj = get_object_or_404(Title, pk=kwargs['pk'])
        # Delete the object
        obj.delete()
        messages.success(self.request, 'Partners deleted successfully.')
        # Redirect to the success URL
        return redirect(self.success_url)
