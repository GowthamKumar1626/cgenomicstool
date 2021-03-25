from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('results/', views.results, name="results"),
    path('results/<str:job_id>', views.job_details, name='job_details')
]