from rest_framework import serializers
from training.models import *


# region Trainee


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id', 'name', 'name_kh', 'gender', 'phone', 'title', 'id_number', 'province', 'operating_district',
                  'facility', 'is_active']


# endregion

# region Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'start_date', 'end_date', 'is_certification', 'certification',
                  'partner_involved', 'province', 'operating_district', 'facility', 'is_active']


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['id', 'name', 'certification_type', 'detail', 'is_active']


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = ['id', 'trainee', 'course', 'register_date', 'province', 'operating_district', 'facility', 'is_active']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'check_date', 'trainee', 'course', 'is_active']
# endregion
