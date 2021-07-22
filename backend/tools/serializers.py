from django.core.validators import MaxLengthValidator
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ToolsModel

class ToolSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = ToolsModel
        fields = ('url', 'name', 'href', 'image', 'description', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'tools')