from rest_framework import serializers

from permission.models import Group, Role


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'user', 'is_active']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'group', 'permission_on', 'permission_data', 'is_active']

