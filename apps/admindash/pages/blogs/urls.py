# urls.py
from django.urls import path
from . import views
app_name = "blogs"

urlpatterns = [
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('list/', views.BlogListView.as_view(), name='list'),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
]
