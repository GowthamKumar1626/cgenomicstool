from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework.response import Response

from results.models import ResultsModel
from results.serializers import ResultsSerializer, UserSerializer
from results.permisions import IsOwner

class ResultsViewSet(viewsets.ModelViewSet):
    queryset = ResultsModel.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner,
    ]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
        
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class UserResultsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    