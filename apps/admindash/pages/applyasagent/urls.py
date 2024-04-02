from django.urls import path, include
from . import views
app_name = "applyasagent"

urlpatterns = [
    path(
        'list/', views.agent_applications, name="list"
    ),
    path(
        'agent_applications/markasread/', views.agent_application_mark_as_read, name="markasread"
    ),
]
