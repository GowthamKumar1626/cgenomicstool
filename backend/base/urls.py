from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('tools/', views.getTools, name="tools"),
    path('tools/<str:pk>/', views.getTool, name="tool"),
]