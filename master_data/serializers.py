from rest_framework import serializers

from master_data.models import *


# region Provice
class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['province', 'description', 'is_active', 'active_date']


class ProvinceKhSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceKh
        fields = ['province', 'description', 'is_active', 'active_date']


# endregion

# region Operating District
class OperatingDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingDistrict
        fields = ['operating_district', 'description', 'is_active', 'active_date']


class OperatingDistrictKhSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingDistrictKh
        fields = ['operating_district', 'description', 'is_active', 'active_date']


# endregion

# region Facility
class FacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityType
        fields = ['id', 'name', 'is_active', 'active_date']


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['facility', 'name', 'type', 'status', 'is_active', 'active_date']


class FacilityKhSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityKh
        fields = ['id', 'facility', 'name', 'type', 'status', 'is_active', 'active_date']
# endregion
