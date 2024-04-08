# urls.py
from django.urls import path
from . import views
app_name = "downloads"

urlpatterns = [
    path('create/', views.DownloadsCreateView.as_view(), name='create'),
    path('list/', views.DownloadsListView.as_view(), name='list'),
    path('<int:pk>/update/', views.DownloadsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DownloadsDeleteView.as_view(), name='delete'),
]
