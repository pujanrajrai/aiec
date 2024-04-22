# urls.py
from django.urls import path
from . import views
app_name = "links"

urlpatterns = [
    path('create/', views.LinksCreateView.as_view(), name='create'),
    path('list/', views.LinksListView.as_view(), name='list'),
    path('<int:pk>/update/', views.LinksUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LinksDeleteView.as_view(), name='delete'),
]
