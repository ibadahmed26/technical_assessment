from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from resume import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("resumes", views.ResumeData, basename="get_resume")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/gettoken/", obtain_auth_token, name="get_token"),
    path("", include(router.urls)),
]
