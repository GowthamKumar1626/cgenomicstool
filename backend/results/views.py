from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ResultModel
from .serializers import ResultsModelSerializer, ResultImagesSerializer
import os
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/results/',
        'api/results?job_id=<pk>/',
    ]
    return Response(routes)

# Tools fetch API
@api_view(["GET"])
def getResults(request):
    results = ResultModel.objects.all()
    serializer = ResultsModelSerializer(results, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getResultDetails(request, pk):
    
    result = ResultModel.objects.get(job_id=pk)
    serializer = ResultsModelSerializer(result, many=False) 

    return Response(serializer.data)

@api_view(["DELETE"])
def deleteResultDetails(request, pk):
    
    result = ResultModel.objects.get(job_id=pk)
    result.delete()
    # serializer = ResultsModelSerializer(result, many=False) 

    return Response(status=status.HTTP_204_NO_CONTENT)


class ResultImages:
    def __init__(self, image):
        self.image = image

@api_view(["GET"])
def resultHeatmap(request):

    image = ResultImages(os.path.join("images", "crosstab-2.png"))
    serializer = ResultImagesSerializer(image)
    return Response(serializer.data)
