from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from tools.models import ToolsModel
from tools.serializers import ToolsSerializer
from tools.permisions import IsOwnerOrReadOnly

from tools import crosstab_test
from results.models import ResultsModel

class ToolsViewSet(viewsets.ModelViewSet):
    queryset = ToolsModel.objects.all()
    serializer_class = ToolsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

@api_view(['GET', 'POST'])
@csrf_exempt
def crosstab(request):
    if request.method == "POST":
        file_path = crosstab_test.load_params(request.data, request.user.id)
        result = ResultsModel(upload_results=file_path, owner=request.user)
        result.save()
        return Response(request.data)
        # return Response(request.data)
    return Response({"message": "Welcome to crosstab tool"})
    
    
"""
{
"id":1,
"genome_column_name": "genome",
}

{
"genome_column_name": "genome",
"gene_column_name":"gene",
"data_format":"CGE",
"chop_genome_name_at":"strain",
"upload_dataset":"/Users/gowthamkumar/Documents/Comparative Genomics/tools/crosstab/datasets/CGE result 10.csv",
"phylo_path":null
}
"""
