# urls.py
from django.urls import path
from . import views
app_name = "subcategory"

urlpatterns = [
    path('create/', views.SubCategoryCreateView.as_view(), name='create'),
    path('list/', views.SubCategoryListView.as_view(), name='list'),
    path('<int:pk>/update/', views.SubCategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.SubCategoryDeleteView.as_view(), name='delete'),
]
