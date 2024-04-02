# urls.py
from django.urls import path
from . import views
app_name = "stories"

urlpatterns = [
    path('create/', views.StoriesCreateView.as_view(), name='create'),
    path('list/', views.StoriesListView.as_view(), name='list'),
    path('<int:pk>/update/', views.StoriesUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.StoriesDeleteView.as_view(), name='delete'),
]
