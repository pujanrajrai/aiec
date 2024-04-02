# urls.py
from django.urls import path
from . import views
app_name = "partners"

urlpatterns = [
    path('create/', views.PartnersCreateView.as_view(), name='create'),
    path('list/', views.PartnersListView.as_view(), name='list'),
    path('<int:pk>/update/', views.PartnersUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PartnersDeleteView.as_view(), name='delete'),
]
