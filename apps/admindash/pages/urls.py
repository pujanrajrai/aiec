from django.urls import path, include
app_name = "pages"
urlpatterns = [
    path(
        'blogs/', include('admindash.pages.blogs.urls')
    ),
    path(
        'studyabroad/', include('admindash.pages.studyabroad.urls')
    ),
    path(
        'services/', include('admindash.pages.services.urls')
    ),
    path(
        'partners/', include('admindash.pages.partners.urls')
    ),
    path(
        'stories/', include('admindash.pages.stories.urls')
    ),
    path(
        'testpreparations/', include('admindash.pages.testpreparations.urls')
    ),
    path(
        'contactus/', include('admindash.pages.contactus.urls')
    ),
    path(
        'applyasstudent/', include('admindash.pages.applyasstudent.urls')
    ),
    path(
        'applyasagent/', include('admindash.pages.applyasagent.urls')
    ),


]
