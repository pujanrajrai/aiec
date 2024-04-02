# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from admindash.models import Title, Category
from .forms import StudyAbroadForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class StudyAbroadCreateView(CreateView):
    model = Title
    form_class = StudyAbroadForm
    template_name = 'studyabroad/create.html'
    success_url = reverse_lazy('admindash:pages:studyabroad:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'studyabroad'
        return context

    def form_valid(self, form):
        default_category = Category.objects.get(name='studyabroad')
        form.instance.category = default_category
        messages.success(self.request, 'studyabroad created successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class StudyAbroadListView(ListView):
    model = Title
    template_name = 'studyabroad/list.html'
    context_object_name = 'studyabroad'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__name="studyabroad")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'studyabroad'
        return context


@method_decorator(login_required, name='dispatch')
class StudyAbroadUpdateView(UpdateView):
    model = Title
    form_class = StudyAbroadForm
    template_name = 'studyabroad/update.html'
    success_url = reverse_lazy('admindash:pages:studyabroad:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'studyabroad'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'studyabroad updated successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class StudyAbroadDeleteView(DeleteView):
    success_url = reverse_lazy('admindash:pages:studyabroad:list')

    def get(self, request, *args, **kwargs):
        # Retrieve the object to delete
        obj = get_object_or_404(Title, pk=kwargs['pk'])
        # Delete the object
        obj.delete()
        messages.success(self.request, 'StudyAbroad deleted successfully.')
        # Redirect to the success URL
        return redirect(self.success_url)
