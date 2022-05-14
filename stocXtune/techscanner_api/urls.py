
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.techscanner_api, name="techscanner_api"),
]