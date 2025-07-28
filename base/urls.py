from django.urls import path
from .views import HomePageData,CreateProfileView

urlpatterns = [
    path('',HomePageData),
    path('createProfile/',CreateProfileView.as_view())
]