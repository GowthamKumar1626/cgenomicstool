from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ToolsModel
from .serializers import ToolsModelSerializer
from .tools import tools
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/tools/',
        'api/tools/crosstab/',
        'api/tools/gene-organisation',
    ]
    return Response(routes)

# Tools fetch API
@api_view(["GET"])
def getTools(request):
    tools = ToolsModel.objects.all()
    serializer = ToolsModelSerializer(tools, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getTool(request, pk):
    
    
    try:
        tool = ToolsModel.objects.get(_id=pk)
        serializer = ToolsModelSerializer(tool, many=False)
    except ValueError:
        try:
            tool = ToolsModel.objects.get(href=pk)
            serializer = ToolsModelSerializer(tool, many=False)
        except Exception as e:
            print(e) 

    return Response(serializer.data)
