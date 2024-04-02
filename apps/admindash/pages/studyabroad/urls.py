# urls.py
from django.urls import path
from . import views
app_name = "studyabroad"

urlpatterns = [
    path('create/', views.StudyAbroadCreateView.as_view(), name='create'),
    path('list/', views.StudyAbroadListView.as_view(), name='list'),
    path('<int:pk>/update/', views.StudyAbroadUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.StudyAbroadDeleteView.as_view(), name='delete'),
]
