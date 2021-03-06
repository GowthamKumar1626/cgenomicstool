from django.core.files.images import ImageFile
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from tools.handlers import validate_data
from tools.crosstab.plots import get_plot
from tools.models import ToolsModel
from tools.serializers import ToolsSerializer
from tools.permisions import IsOwnerOrReadOnly

from tools import crosstab_test
from results.models import ResultsModel
from tools.handlers import extract_column_names

import pandas as pd
import json

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
        try:
            data = validate_data(request)
            result_stamp = crosstab_test.load_params(data, request.user.id)
            
            
            result = ResultsModel.objects.create(result_id=result_stamp, upload_results=f"files/{result_stamp}.csv", image=ImageFile(open(f"./static/images/{result_stamp}.jpeg", "rb")), owner=request.user)
            result.save()
            
            return Response({"result_id": result.result_id, "created_at": result.created_at})
        except Exception as error:
            return Response({"detail": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # return Response(request.data)
    return Response({"message": "Welcome to crosstab tool"})


@api_view(['GET', 'POST'])
@csrf_exempt
def columnNamesCrosstabDataset(request):
    if request.method == "POST":
        # column_names = extract_column_names()
        if str(request.FILES['dataset']).count("sv")>0:
            return Response(list(pd.read_csv(request.FILES['dataset']).columns.values))
        else:
            return Response(list(pd.read_excel(request.FILES['dataset']).columns.values))
    return Response({"message": "Welcome to crosstab tool column names finder"})
    
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def crosstabPlot(request, pk):
    plot_path = get_plot(ResultsModel.objects.get(result_id=pk).upload_results)
    return Response({"url": plot_path})





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
