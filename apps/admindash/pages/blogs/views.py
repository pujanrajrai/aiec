# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from admindash.models import Title, Category
from .forms import BlogForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = Title
    form_class = BlogForm
    template_name = 'blogs/create.html'
    success_url = reverse_lazy('admindash:pages:blogs:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'blogs'
        return context

    def form_valid(self, form):
        default_category = Category.objects.get(name='blogs')
        form.instance.category = default_category
        messages.success(self.request, 'blogs created successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogListView(ListView):
    model = Title
    template_name = 'blogs/list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__name="blogs")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'blogs'
        return context


@method_decorator(login_required, name='dispatch')
class BlogUpdateView(UpdateView):
    model = Title
    form_class = BlogForm
    template_name = 'blogs/update.html'
    success_url = reverse_lazy('admindash:pages:blogs:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'master'
        context['current'] = 'blogs'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'blogs updated successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogDeleteView(DeleteView):
    success_url = reverse_lazy('admindash:pages:blogs:list')

    def get(self, request, *args, **kwargs):
        # Retrieve the object to delete
        obj = get_object_or_404(Title, pk=kwargs['pk'])
        # Delete the object
        obj.delete()
        messages.success(self.request, 'Blog deleted successfully.')
        # Redirect to the success URL
        return redirect(self.success_url)
