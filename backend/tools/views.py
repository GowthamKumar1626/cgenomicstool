from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tools.models import ToolsModel
from tools.serializers import ToolsSerializer
from tools.permisions import IsOwnerOrReadOnly

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

@api_view(['POST'])
def crosstab(request):
    if request.method == "POST":
        print(request.data)
        return Response({"message": "Hello! crosstab"})