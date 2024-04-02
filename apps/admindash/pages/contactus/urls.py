from django.urls import path, include
from . import views
app_name = "contactus"

urlpatterns = [
    path(
        'list/', views.contact_us, name="list"
    ),
    path(
        'contact/markasread/', views.contactus_mark_as_read, name="markasread"
    ),
]
