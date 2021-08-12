from django.urls.conf import path

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.reverse import reverse

from base.views import MyTokenObtainPairView, getUsers, getUserProfile, registerUser, updateUserProfile
from tools.views import ToolsViewSet, crosstab, columnNamesCrosstabDataset, crosstabPlot
from results.views import ResultsViewSet, UserResultsViewSet, FileDownloadListAPIView


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
        'users': reverse('users', request=request, format=format),
        'user-login': reverse('user-login', request=request, format=format),
        'user-register': reverse('user-register', request=request, format=format),
        'user-profile': reverse('user-profile', request=request, format=format),
        'user-profile-update': reverse('user-profile-update', request=request, format=format),
        'users-results': reverse('user-results-list', request=request, format=format),
        'crosstab': reverse('crosstab', request=request, format=format),
        'crosstab-process-inputs': reverse('crosstab', request=request, format=format),
        'crosstab-plot': reverse('crosstab-plot', request=request, format=format),
    })


## URLPATTERNS 

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('tools/', tools_list, name='tools-list'),
    path('tools/<str:pk>/', tool_detail, name='toolsmodel-detail'),
    path('results/', result_list, name='results-list'),
    path('results/<str:pk>/', result_detail, name='resultsmodel-detail'),
    path('results/<str:id>/download/', FileDownloadListAPIView.as_view(), name="result-download"),
    path('users/', getUsers, name='users'),
    path('users/login/', MyTokenObtainPairView.as_view(), name='user-login'),
    path('users/register/', registerUser, name='user-register'),
    path('users/profile/', getUserProfile, name='user-profile'),
    path('users/profile/update/', updateUserProfile, name='user-profile-update'),
    path('users/results/', user_list, name='user-results-list'),
    path('users/<int:pk>/', user_results, name='user-detail'),
    path('crosstab/', crosstab, name="crosstab"),
    path('crosstab/process-inputs/', columnNamesCrosstabDataset, name="crosstab"),
    path('crosstab/plot/<str:pk>/', crosstabPlot, name='crosstab-plot')
])