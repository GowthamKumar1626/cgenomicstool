from django.urls.conf import path

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.reverse import reverse

from tools.views import ToolsViewSet
from results.views import ResultsViewSet, UserResultsViewSet

## Tools Routes

tools_list = ToolsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
tool_detail = ToolsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

## Result Routes

result_list = ResultsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
result_detail = ResultsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

## User Routes

user_list = UserResultsViewSet.as_view({
    'get': 'list'
})
user_results = UserResultsViewSet.as_view({
    'get': 'retrieve'
})



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tools': reverse('tools-list', request=request, format=format),
        'results': reverse('results-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })


## URLPATTERNS 

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('tools/', tools_list, name='tools-list'),
    path('tools/<str:pk>/', tool_detail, name='toolsmodel-detail'),
    path('results/', result_list, name='results-list'),
    path('results/<str:pk>/', result_detail, name='resultsmodel-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_results, name='user-detail')
])