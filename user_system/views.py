from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from user_system.models import User
from user_system.serializers import UserCreateSerializer, UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response({"message": "Request Body Error"}, status=status.HTTP_409_CONFLICT)

    if User.objects.filter(username=serializer.validated_data['username']).first() is None:
        serializer.save()
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)
    return Response({"message": "duplicate username"}, status=status.HTTP_409_CONFLICT)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
