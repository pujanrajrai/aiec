from django.urls import path, include
from . import views
app_name = "frontend"
urlpatterns = [
    path(
        "", views.home, name="home"
    ),
    path(
        "title/<str:pk>", views.title, name="title"
    ),
    path(
        "aboutus/", views.aboutus, name="aboutus"
    ),
    path(
        "allblogs/", views.allblogs, name="allblogs"
    ),
    path(
        "contactus/", views.contactus, name="contactus"
    ),
    path(
        "applyasstudent/", views.applyasstudent, name="applyasstudent"
    ),
    path(
        "applyasagent/", views.applyasagent, name="applyasagent"
    ),

]
