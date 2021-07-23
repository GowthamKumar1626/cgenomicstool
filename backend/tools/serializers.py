from django.contrib.auth.models import User

from rest_framework import serializers
from tools.models import ToolsModel

class ToolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToolsModel
        fields = ['url', 'name', 'image', 'description',]

