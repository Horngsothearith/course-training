from django.urls import path

from master_data import views

urlpatterns = [
    path('create_province', views.create_province, name='create_province'),
    path('create_province_kh', views.create_province_kh, name='create_province_kh'),
    path('create_operating_district', views.create_operating_district, name='create_operating_district'),
    path('create_operating_district_kh', views.create_operating_district_kh, name='create_operating_district_kh'),
    path('create_facility_type', views.create_facility_type, name='create_facility_type'),
    path('create_facility', views.create_facility, name='create_facility'),
    path('create_facility_kh', views.create_facility_kh, name='create_facility_kh'),
    # get
    # all
    path('get_all_province', views.get_all_province, name='get_all_province'),
    path('get_all_operating_district', views.get_all_operating_district, name='get_all_operating_district'),
    path('get_all_facility', views.get_all_facility, name='get_all_facility'),
    path('get_operating_district_by_province', views.get_operating_district_by_province, name='get_operating_district_by_province'),
    path('get_facility_by_operating_district', views.get_facility_by_operating_district, name='get_facility_by_operating_district'),
]
