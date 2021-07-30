from django.contrib.auth.models import User

from rest_framework import serializers
from results.models import ResultsModel

class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CreateOnlyDefault(default='owner.username')
    result_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ResultsModel
        fields = "__all__"
    
    def get_result_id(self, obj):
        return obj.result_id
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    results = serializers.HyperlinkedRelatedField(many=True, view_name='resultsmodel-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'results']