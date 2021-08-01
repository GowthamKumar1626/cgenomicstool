from django.contrib.auth.models import User
from django.http import HttpResponse

from wsgiref.util import FileWrapper

from rest_framework import viewsets, permissions, generics

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

class FileDownloadListAPIView(generics.ListAPIView):

    def get(self, request, id, format=None):
        queryset = ResultsModel.objects.get(result_id=id)
        file_handle = queryset.upload_results.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.upload_results.name
        return response