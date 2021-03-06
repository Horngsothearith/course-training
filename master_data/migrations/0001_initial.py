# Generated by Django 3.2.3 on 2021-05-30 01:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('active_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityKh',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('facility', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('type', models.TextField()),
                ('status', models.CharField(max_length=255)),
                ('active_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('active_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingDistrict',
            fields=[
                ('operating_district', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('active_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingDistrictKh',
            fields=[
                ('operating_district', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('active_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('province', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('active_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProvinceKh',
            fields=[
                ('province', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('active_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
