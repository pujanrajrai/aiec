# urls.py
from django.urls import path
from . import views
app_name = "testpreparations"

urlpatterns = [
    path('create/', views.TestPreparationCreateView.as_view(), name='create'),
    path('list/', views.TestPreparationListView.as_view(), name='list'),
    path('<int:pk>/update/', views.TestPreparationUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TestPreparationDeleteView.as_view(), name='delete'),
]
