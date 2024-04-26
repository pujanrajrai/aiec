from django.urls import path, include
from . import views
app_name = "admindash"
urlpatterns = [
    path(
        'login/', views.login, name="login"
    ),
    path(
        'logout/', views.logout, name="logout"
    ),
    path(
        'pages/', include('admindash.pages.urls')
    )
]
