# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from permission.serializers import *


# region Create
@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_group(request):
    name = request.POST.get('name')
    user_id = request.POST.get('user_id')
    if not name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not user_id:
        return Response({'code': '400', 'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(id=user_id)
    try:
        '''Return error'''
        Group.objects.get(name=name)
        return Response({'code': '400', 'error': 'Group has already existed!'}, status=status.HTTP_400_BAD_REQUEST)
    except Group.DoesNotExist:
        '''Create if Don't have'''
        obj = Group.objects.create(name=name, user=user)
        serializer = GroupSerializer(obj)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def create_role(request):
    name = request.POST.get('name')
    group = request.POST.get('group')
    permission_on = request.POST.get('permission_on')
    permission_data = request.POST.get('permission_data')
    if not name:
        return Response({'code': '400', 'error': 'name is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not group:
        return Response({'code': '400', 'error': 'group is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not permission_on:
        return Response({'code': '400', 'error': 'permission_on is required'}, status=status.HTTP_400_BAD_REQUEST)
    if not permission_data:
        return Response({'code': '400', 'error': 'permission_data is required'}, status=status.HTTP_400_BAD_REQUEST)
    group = Group.objects.get(id=group)
    try:
        '''Return error'''
        Role.objects.get(name=name, permission_on=permission_on, permission_data=permission_data)
        return Response({'code': '400', 'error': 'Group has already existed!'}, status=status.HTTP_400_BAD_REQUEST)
    except Role.DoesNotExist:
        '''Create if Don't have'''
        obj = Role.objects.create(name=name, group=group, permission_on=permission_on, permission_data=permission_data)
        serializer = RoleSerializer(obj)
        return Response(serializer.data)
# endregion

# region Get
# region all

@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_group(request):
    user = request.user
    if user.is_superuser:
        obj = Group.objects.all()

        serializer = GroupSerializer(obj, many=True)
        return Response(serializer.data)
    Response({'code': '403', 'error': 'Access Denied!'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_role(request):
    user = request.user
    if user.is_superuser:
        obj = Role.objects.all()

        serializer = RoleSerializer(obj, many=True)
        return Response(serializer.data)
    Response({'code': '403', 'error': 'Access Denied!'}, status=status.HTTP_403_FORBIDDEN)
# endregion
# endregion
