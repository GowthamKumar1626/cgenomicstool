from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoutes, name="routes"),
    path('results/', views.getResults, name="results"),
    path('results/<str:pk>/', views.getResultDetails, name="result_details"),
    path('results/<str:pk>/delete/', views.deleteResultDetails, name="delete_result_details"),
    path('image/', views.resultHeatmap, name="result_heatmap"),
]