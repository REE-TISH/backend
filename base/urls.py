from django.urls import path
from .views import HomePageData

urlpatterns = [
    path('',HomePageData)
]