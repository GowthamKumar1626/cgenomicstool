from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ResultModel


class ResultsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultModel
        fields = "__all__"

class ResultImagesSerializer(serializers.Serializer):
    image = serializers.CharField(max_length = 200)
