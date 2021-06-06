import uuid

from django.db import models

# Create your models here.


class Trainee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)
    name_kh = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    province = models.TextField()
    operating_district = models.TextField()
    facility = models.TextField()
    is_active = models.BooleanField(default=True)


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_certification = models.BooleanField(default=True)
    certification = models.TextField()
    partner_involved = models.TextField()
    province = models.TextField()
    operating_district = models.TextField()
    facility = models.TextField()
    is_active = models.BooleanField(default=True)


class CourseRegistration(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    trainee = models.TextField()
    course = models.TextField()
    register_date = models.DateTimeField(auto_now=True)
    province = models.TextField()
    operating_district = models.TextField()
    facility = models.TextField()
    is_active = models.BooleanField(default=True)


class Certification(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)
    certification_type = models.CharField(max_length=255)
    detail = models.TextField()
    is_active = models.BooleanField(default=True)


class Attendance(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    check_date = models.DateTimeField(auto_now=True)
    trainee = models.TextField()
    course = models.TextField()
    is_active = models.BooleanField(default=True)