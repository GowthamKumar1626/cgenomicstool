from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import serializers, permissions, renderers, viewsets, status
from rest_framework.serializers import Serializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.reverse import reverse

from rest_framework import mixins
from rest_framework import generics

from .models import ToolsModel
from .serializers import ToolSerializer, UserSerializer

from tools.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

## Using generic class-based views

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tools': reverse('tool-list', request=request, format=format)
    })

class ToolViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ToolsModel.objects.all()
    serializer_class = ToolSerializer
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly, 
        )

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def description(self, request, *args, **kwargs):
        tool = self.get_object()
        return tool(tool.description)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



# Using Mixins
 
# class ToolList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     """
#     Lists all tools available in CGenomcis tool or create a new Tool
#     """
    
#     queryset = ToolsModel.objects.all()
#     serializer_class = ToolsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
        
# class ToolDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     """
#     Retrieve, update, delete the respective tool
#     """
            
#     queryset = ToolsModel.objects.all()
#     serializer_class = ToolsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs) 
    


## Using Class-Based APIViews

# class ToolsList(APIView):
#     """
#     Lists all tools available in CGenomcis tool or create a new Tool
#     """
#     def get(self, request, format=None):
#         tools = ToolsModel.objects.all()
#         serializer = ToolsSerializer(tools, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = ToolsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# class ToolDetails(APIView):
#     """
#     Retrieve, update, delete the respective tool
#     """
#     def get_object(self, pk):
#         try:
#             return ToolsModel.objects.get(href=pk)
#         except ToolsModel.DoesNotExist:
#             return Http404
            
#     def get(self, request, pk, format=None):
#         tool = self.get_object(pk)
#         serializer = ToolsSerializer(tool)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         tool = self.get_object(pk)
#         serializer = ToolsSerializer(tool, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         tool = self.get_object(pk)
#         tool.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
           
    
## Using function based views

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def tools_list(request, format=None):
#     """
#     Lists all tools available in CGenomcis tool
#     """
#     if request.method == "GET":
#         tools = ToolsModel.objects.all()
#         serializer = ToolsSerializer(tools, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ToolsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt 
# @api_view(['GET', 'PUT', 'DELETE'])      
# def tool_details(request, pk, format=None):
#     """
#     Function helps to retrieve, update, delete the respective tool
#     """
    
#     try:
#         tool = ToolsModel.objects.get(pk=pk)
#     except ToolsModel.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     # Case for retreiving the data
#     if request.method == "GET":
#         serializer = ToolsSerializer(tool)
#         return Response(serializer.data)
    
#     # Case for updating the data
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = ToolsSerializer(tool, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     # Case for deleting th data
#     elif request.method == "DELETE":
#         tool.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)