from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ToolsModel


class ToolsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolsModel
        fields = "__all__"