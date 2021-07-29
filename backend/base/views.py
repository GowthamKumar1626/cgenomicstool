from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from base.serializers import MyTokenObtainPairSerializer, UserSerializer, UserSerializerWithToken


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["POST"])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data["email"],
            password = make_password(data["password"])
        )
        serializer = UserSerializerWithToken(user)
        return Response(serializer.data)
    except:
        message = {"details": "User with this email already exist"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)