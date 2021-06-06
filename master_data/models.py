import uuid

from django.db import models


# Create your models here.


class Province(models.Model):
    province = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    description = models.CharField(max_length=255)
    active_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)


class ProvinceKh(models.Model):
    province = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    description = models.CharField(max_length=255)
    active_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)


class OperatingDistrict(models.Model):
    operating_district = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    description = models.CharField(max_length=255)
    active_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)


class OperatingDistrictKh(models.Model):
    operating_district = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    description = models.CharField(max_length=255)
    active_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)


class FacilityType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)
    active_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Facility(models.Model):
    facility = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)
    type = models.TextField()
    status = models.CharField(max_length=255)
    active_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)


class FacilityKh(models.Model):
    facility = models.CharField(max_length=10, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255)
    type = models.TextField()
    status = models.CharField(max_length=255)
    active_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)