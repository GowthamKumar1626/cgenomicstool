from results.serializers import ResultsSerializer
from results.models import ResultsModel
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ["id", "_id", "username", "email", "name", "isAdmin"]
        
    def get__id(self, obj):
        return obj.id
        
    def get_isAdmin(self, obj):
        return obj.is_staff
    
    def get_name(self, obj):
        try:
            name = obj.first_name
        except AttributeError as error:
            try:
                name =  obj.email
            except AttributeError as error:
                name = obj.username
        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ["id", "_id", "username", "email", "name", "isAdmin", "token"]
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        
        for key, value in serializer.items():
            data[key] = value

        return data