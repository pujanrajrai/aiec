from django.urls import path, include
from . import views
app_name = "frontend"
urlpatterns = [
    path(
        "", views.home, name="home"
    ),
    path(
        'admin/', views.admin, name="login"
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
    path(
        "downloads/", views.downloads, name="downloads"
    ),
    path(
        "downloads/<str:sub_category>", views.downloads_details, name="downloads_details"
    ),
    path(
        "<str:slug>/", views.title, name="title"
    ),


]
