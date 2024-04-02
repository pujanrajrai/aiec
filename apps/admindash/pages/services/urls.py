# urls.py
from django.urls import path
from . import views
app_name = "services"

urlpatterns = [
    path('create/', views.ServicesCreateView.as_view(), name='create'),
    path('list/', views.ServicesListView.as_view(), name='list'),
    path('<int:pk>/update/', views.ServicesUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ServicesDeleteView.as_view(), name='delete'),
]
