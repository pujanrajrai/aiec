from django.urls import path, include
from . import views
app_name = "applyasstudent"

urlpatterns = [
    path(
        'list/', views.student_applications, name="list"
    ),
    path(
        'student_applications/markasread/', views.student_application_mark_as_read, name="markasread"
    ),
]
