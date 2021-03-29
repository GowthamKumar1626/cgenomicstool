from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('results/', views.results, name="results"),
    path('results/<str:job_id>/overview/', views.job_details, name='job_details'),
    path('results/<str:job_id>/<str:gene_name>/', views.genome_info, name='genome-info'),
    path('delete/<str:job_id>/', views.delete_job, name="delete-job"),
]