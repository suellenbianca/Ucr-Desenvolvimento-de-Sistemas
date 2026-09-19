from .import views

from django.urls import path

urlpatterns = [
    path('inicial', views.home)
]