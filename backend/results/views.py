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
    def get_queryset(self):
        return ResultsModel.objects.filter(owner=self.request.user.id)


class UserResultsViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    