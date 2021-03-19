from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='crosstab'),
    path('about/', views.about, name='crosstab-about'),
]
